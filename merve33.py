def sayi_al():
    liste=[]
    while True:
        veri=input("Sayi girin cikmak icin'q'yazin\n")
        if veri=="q":
            print("Girdi tamamlandi")
            break
        try:
            sayi=float(veri)
            liste.append(sayi)
        except ValueError:
            print("Yeniden Deneyiniz")
    return liste

sayilar=sayi_al()   
print("Girilen sayilar:",sayilar)
while True:
    secim=input("Seciminiz")
    if secim=="1":
        al=[x for x in sayilar if x>0]
        print("Pozitif sayilar:",al)
    elif secim=="2":
        all=[x for x in sayilar if x<0]
        print("Negatif sayilar",all)
    elif secim=="3":
        can=[x for x in sayilar if x%2!=0]
        print("Tek sayilar",can)
    elif secim =="4":
            canan=[x for x in sayilar if x%2==0]
            print("Cift sayilar",canan)
    elif secim=="5":
            print("Ortalama deger",sum(sayilar)/len(sayilar))
    elif secim=="6":
        print("En buyuk sayi:",max(sayilar))
        print("En kucuk sayi:",min(sayilar))
        
    elif secim=="q":
        break
print("sayilar listesi",sayilar)
        



                


