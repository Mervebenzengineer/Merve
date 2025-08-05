#sayilar=[-2,-5,-9,23,0,8]
#mutlak_deger=[abs(x) for x in sayilar] 
#print("Mutlak degerli sayilar",mutlak_deger)

def sayi_al():
    negatifler=[]
    while True:
        veri=input("Sayi girin(cikmak icin'q'):")
        if veri=="q":
            print("Girdi islemi sona erdi\n")
            break
        try:
            sayi=float(veri)
            if sayi<0:
                negatifler.append(sayi)
        except ValueError:
            print("Gecerli sayi girin")
    return negatifler

negatif_sayilar=sayi_al()
mutlaklar=[abs(x)for x in negatif_sayilar]
print("Negatif sayilar:",negatif_sayilar)
print("Mutlak degerli sayilar:",mutlaklar)