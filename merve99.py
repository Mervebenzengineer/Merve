import numpy as np   # NumPy kütüphanesini içe aktarıyoruz (matematiksel işlemler ve diziler için)
import json          # JSON formatında veri kaydetmek/okumak için json kütüphanesi

# 8 öğrenci ve 5 ders için 0-99 arası rastgele notlardan oluşan 8x5 matris oluşturuyoruz
notlar = np.random.randint(0, 100, size=(8, 5))

print("Notlar matrisi:", notlar)  # Tüm not matrisini ekrana yazdır

# axis=0 → sütunlar bazında işlem yapar, her dersin ortalamasını verir
print("Her ders ortalamasi:", np.mean(notlar, axis=0))

# Tüm sınıfın genel ortalaması
print("Sinif genel ortalamasi:", np.mean(notlar))

# Minimum değer (en düşük not)
print("Notlarin minumum degeri:", np.min(notlar))

# Maksimum değer (en yüksek not)
print("Notlarin maksimum degeri:", np.max(notlar))

# Standart sapma → notların dağılımını ölçer
print("Standart sapmasi:", np.std(notlar))

# En yüksek notun dizideki (tek boyutlu) indeksini bul
max_index = np.argmax(notlar)

# np.unravel_index → tek boyutlu indeks değerini (satır, sütun) konumuna çevirir
ogrenci_max, ders_max = np.unravel_index(max_index, notlar.shape)

# En yüksek notu ve hangi öğrenci/ders olduğunu yazdır
print(f"En yuksek not {notlar[ogrenci_max, ders_max]} (Ogrenci {ogrenci_max+1}, Ders {ders_max+1})")

# En düşük notun dizideki indeksini bul
min_index = np.argmin(notlar)

# Tek boyutlu indeksi satır/sütun formatına çevir
ogrenci_min, ders_min = np.unravel_index(min_index, notlar.shape)

# En düşük notu ve hangi öğrenci/ders olduğunu yazdır
print(f"En dusuk not {notlar[ogrenci_min, ders_min]} (Ogrenci {ogrenci_min+1}, Ders {ders_min+1})")

# CSV dosyasına kaydet (header kısmı sütun başlıkları, comments="" → başına # eklenmesini engeller)
np.savetxt("notlar.csv", notlar, fmt="%d", delimiter=",", header="Ders1,Ders2,Ders3,Ders4,Ders5", comments="")

print("\nNotlar 'notlar.csv' dosyasina kaydedildi.")

# CSV dosyasını tekrar oku (skiprows=1 → başlığı atla)
okunan_csv = np.loadtxt("notlar.csv", delimiter=",", skiprows=1, dtype=int)
print("\nDosyadan Okunan Notlar", okunan_csv)

# JSON formatında kaydet (tolist() → NumPy array → Python list)
with open("notlar.json", "w") as dosya:
    json.dump(notlar.tolist(), dosya)

print("\nNotlar 'notlar.json' dosyasina kaydedildi.")

# JSON formatında oku
with open("notlar.json", "r") as dosya:
    okunan_json = json.load(dosya)

print("\nJSON'dan Okunan Notlar:\n", okunan_json)








#En yüksek notun hangi öğrenci ve derste olduğu bulundu (np.unravel_index).

#np.argmin() → en küçük değerin indeksini verir.

#np.unravel_index() → düz indeks → matrisin satır/sütun konumuna çevirir