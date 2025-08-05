isim=input("Isminizi girin:")
sifre=input("Sifrenizi girin:")
giris_yapildi_mi=False
if not giris_yapildi_mi:
    if(isim=="Merve" and sifre==4731) or isim=="admin":
        print("Giris basarili,hos geldiniz!")
        giris_yapildi_mi=True
    else:
        print("Hatali giris!Lutfen tekrar deneyin.")
else:
    print("Zaten giris yaptiniz")
    