toplam=0
print("Sayi girin.Cikmak icin'q' yazin.")

while True:
    veri=input("Sayi:")
    if veri=="q":
        print("Dongu sonlandirildi")
        break
    
    if veri.isdigit():
        toplam += int(veri)
    else:
        print("Sayi girmeniz gerekiyor")
        
print("Toplam sonuc:",toplam)

