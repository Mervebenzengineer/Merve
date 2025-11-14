import os

if not os.path.exists("proje"):
    os.mkdir("proje")
    print("Klasor olusturuldu.")
else:
    print("Klasor mevcut.")

dosya_yolu=os.path.join("proje","veri.txt")

with open(dosya_yolu,"w") as dosya:
    dosya.write("Bir test dosyasidir.")
print("Dosya olusturuldu:",dosya_yolu)

if os.path.exists(dosya_yolu):
    os.remove(dosya_yolu)
    print("Dosya silindi.")

if os.path.exists("proje"):
    os.rmdir("proje")
    print("Klasor silindi.")


"""
os.path.exists() → Dosya ya da klasör var mı kontrol eder.
os.mkdir() → Klasör oluşturur.
os.path.join() → Yol birleştirme yapar (platform bağımsız).
os.remove() → Dosyayı siler.
os.rmdir() → Boş klasörü siler.
"""