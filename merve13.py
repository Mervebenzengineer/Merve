#sayi=1
#while sayi<=5:
 #   print(sayi)
 #   sayi+=1#
#sifre=""
#while sifre!="merve2025":
 #   sifre=input("Sifreyi girin:")
#print("Giris basarili")

dogru_sifre="merve2025"
hak=3 #3 hak var
while hak>0:#hak 0 oluncaya dek devam
    girilen_sifre=input("Sifreyi girin:")
    if girilen_sifre==dogru_sifre:#sifre dogruysa dongu durur
        print("Giris basarili!")
        break
    else:#sifre yanlissa hak 1 azalir
        hak-=1
        print("Yanlis sifre.Kalan hak:",hak)
if hak==0:#hak bitince uyari verir
    print("Hesabiniz kilitlendi.Daha sonra tekrar deneyin.")
