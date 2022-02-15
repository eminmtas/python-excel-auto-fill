from pandas import DataFrame
from datetime import date, timedelta

#Hafta sonu olup olmadığını kontrol eden fonksiyon
def isWeekend(tarih):
    weekday = ["Moday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    weekend = ["Saturday", "Sunday"]
    
    if set(tarih.strftime("%A")).issubset(str(weekday)):
        haftasonuMu.append(0)
        #pazartesi ve cuma günleri için
        if set(tarih.strftime("%A")).issubset("Monday"):
            pazartesi.append(1)
        else:
            pazartesi.append(0)
        if set(tarih.strftime("%A")).issubset("Friday"):
            cuma.append(1)
        else:
            cuma.append(0)

    if set(tarih.strftime("%A")).issubset(str(weekend)):
        haftasonuMu.append(1)
        pazartesi.append(0)
        cuma.append(0)

#Tarih aralığını gün-ay-yıl olarak ayrı ayrı alma
print("Başlangıç tarihini giriniz:")
gun_i = int(input("Gün:"))
ay_i = int(input("Ay:"))
yil_i = int(input("Yıl:"))
print("\nBitiş tarihini giriniz:")
gun_s = int(input("Gün:"))
ay_s = int(input("Ay:"))
yil_s = int(input("Yıl:"))

#Dosyaya isim verme
dosyaismi = str(input("Dosya ismi giriniz:")) + ".xlsx"

#Değişkenler
gunler = []
aylar = []
yillar = []
haftasonuMu = []
pazartesi = []
cuma = []

#Tarihler arası fark oluşturma
ilkTarih = date(yil_i, ay_i, gun_i)
sonTarih = date(yil_s, ay_s, gun_s)
tarihFarki = sonTarih - ilkTarih

for i in range(tarihFarki.days + 1):
    tarih = ilkTarih + timedelta(days=i)

    if tarih.day in range(1,10):
        gunler.append(str("0") + str(tarih.day))
    else:
        gunler.append(tarih.day)
    if tarih.month in range(1,10):
        aylar.append(str("0") + str(tarih.month))
    else:
        aylar.append(tarih.month)
    yillar.append(tarih.year)
    isWeekend(tarih)

d = {"Gün": gunler, "Ay": aylar, "Yıl": yillar, "Weekend?": haftasonuMu, "Pazartesi": pazartesi, "Cuma": cuma}
df = DataFrame(data=d)
df.to_excel(dosyaismi, sheet_name="Sayfa 1", index=False) #index true dersek satır numaralarını yazacak
