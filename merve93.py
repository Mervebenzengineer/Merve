import os

klasor="."
dosyalar=os.listdir(klasor)

print("Klasordeki dosyalar:")
for dosya in dosyalar:
    print(dosya)

#"." = "Şu anda içinde bulunduğum klasör" 