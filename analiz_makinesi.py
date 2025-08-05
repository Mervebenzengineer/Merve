def sayilar():
    liste=[]
    while True:
        veri=(input("sayi girin(cikmak icin'q' yazin):"))
        if veri=="q":
         print("Tekrar sayi girin")
         break
        try:
            sayi=float(veri)
            liste.append(sayi)
       
        except ValueError:
            print("Sayi girilemedi")
    return liste
liste=sayilar()

pozitif_sayi=[x for x in liste if x>0]
print("pozitif sayilar",pozitif_sayi)

negatif_sayilar=[x for x in liste if x<0]
print("Negatif sayi",negatif_sayilar)

mutlak_deger=[abs(x) for x in negatif_sayilar]
print("Mutlak deger",mutlak_deger)

print("Max deger",max(liste))

print("Min deger",min(liste))






          

       
       
   
