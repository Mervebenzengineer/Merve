# Kullanıcıdan isim ve şifre alma
isim = input("Isminizi girin: ")
sifre = int(input("Sifrenizi girin: "))

# Başlangıçta giriş yapılmadı
giris_yapildi_mi = False

# Eğer giriş yapılmadıysa
if not giris_yapildi_mi:
    # İsim ve şifre kontrolü
    if (isim == "Merve" and sifre == 4731) or isim == "admin":
        print("Giris basarili, hos geldiniz!")
        giris_yapildi_mi = True
    else:
        print("Hatali giris! Lutfen tekrar deneyin.")
# Eğer zaten giriş yapılmışsa
else:
    print("Zaten giris yaptiniz.")

