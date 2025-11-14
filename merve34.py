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
            print("Yeniden Deneyiniz!")
    return liste

sayilar=sayi_al()   
print("Girilen sayilar:",sayilar)

def pozitifleri_goster(sayilar):
    can=[x for x in sayilar if x>0]
    print("Pozitif sayilar",can)

def negatifleri_goster(sayilar):
    canan=[x for x in sayilar if x<0]
    print("Negatif sayilar",canan)

def ortalama_hesapla(sayilar):
   print("Ortalama",sum(sayilar)/len(sayilar))

def tek_sayilari_goster(sayilar):
    al=[x for x in sayilar if x%2!=0]
    print("Tek sayilar",al)

def cift_sayilari_goster(sayilar):
    ala=[x for x in sayilar if x%2==0]
    print("Cift sayilar")


while True:
    secim=input("Seciminiz:")
    if secim=="1":
        pozitifleri_goster(sayilar)
    elif secim=="2":
        negatifleri_goster(sayilar)
    elif secim=="3":
        ortalama_hesapla(sayilar)
    elif secim=="4":
        tek_sayilari_goster(sayilar)
    elif secim=="5":
        cift_sayilari_goster(sayilar)
    elif secim=="6":
        with open("sayilar.txt","w") as dosya:
            for sayi in sayilar:
                dosya.write(str(sayi)+"\n")
            print("Sayilar dosyaya yazildi")
    elif secim=="7":
            try:
                with open("sayilar.txt","r") as dosya:
                    satirlar=dosya.readlines()
                    okunanlar=[]
                    for satir in satirlar:
                        sayi=float(satir.strip())
                        okunanlar.append(sayi)
                    print("Dosyadan okunan sayilar:",okunanlar)
            except  ValueError:
                print("Dosya bulunamadi.Once dosyaya veri yazmalisiniz.")

    elif secim=="q":
        break



            