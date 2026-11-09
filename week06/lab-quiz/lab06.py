branslar = ("Yazılım", "Tasarım", "Pazarlama")

tum_ogrenciler = []

ogrenci_1 = ["  Ahmet Yılmaz  ".strip(), [branslar[0], branslar[1]]]
ogrenci_2 = [" Ayşe Kaya ".strip(), [branslar[1]]]
ogrenci_3 = ["Mehmet Demir   ".strip(), [branslar[0], branslar[2]]]

tum_ogrenciler.append(ogrenci_1)
tum_ogrenciler.append(ogrenci_2)
tum_ogrenciler.append(ogrenci_3)


baskan = ["Erdinç Kılıç".strip(), [branslar[0]]]
tum_ogrenciler.insert(0, baskan)


print(f"Toplam Kayıtlı Öğrenci Sayısı: {len(tum_ogrenciler)}")


tum_ogrenciler.remove(["Ayşe Kaya", [branslar[1]]])

cikan_ogrenci = tum_ogrenciler.pop()
print(f"Sistemden en son çıkan öğrenci: {cikan_ogrenci[0]}")

yeni_ogrenci = ["Burak Tan".strip(), [branslar[1]]]
tum_ogrenciler.append(yeni_ogrenci)

gecici_sirali = sorted(tum_ogrenciler)
print("\n--- sorted() ile Geçici Sıralı Liste ---")
print(gecici_sirali)

print("\n--- Orijinal Listenin Değişmediğinin Kanıtı ---")
print(tum_ogrenciler)


tum_ogrenciler.sort()
print("\n--- sort() Sonrası Kalıcı Olarak Sıralanmış Liste ---")
print(tum_ogrenciler)
