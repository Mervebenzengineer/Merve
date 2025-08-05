hak = 3  # Kullanıcının 3 deneme hakkı var

while hak > 0:
    isim = input("İsminiz nedir? ")
    sifre = int(input("Şifrenizi girin: "))

    if (isim == "Merve" and sifre == 4732) or (isim == "admin"):
        print("Hoş geldiniz!")
        break  # Giriş başarılıysa döngüyü kır
    else:
        hak -= 1  # Hatalı girişte hak azalt
        if hak > 0:
            print(f"Hatalı giriş! Kalan hakkınız: {hak}")
        else:
            print("Giriş hakkınız doldu.")




