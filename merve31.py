def sayilari_al():
    liste=[]
    while True:
     veri=input("Sayi girin. 'q' yazinca cikin")
     if veri=="q":
         break 
     try:
             sayi=float(veri)
             liste.append(sayi)
     except ValueError:
         print("Gecerli sayi girin")

    return liste
def analiz_et(sayilar):
    if not sayilar:
        print("Hic sayi girilmedi")
        return
    pozitifler=[x for x in sayilar if x>0]
    negatifler=[x for x in   sayilar if x<0]
    mutlaklar=[abs(x) for x in negatifler]
    print("Ortalama",sum(sayilar)/len(sayilar))
    print("En buyuk sayi:",max(sayilar))
    print("En kucuk sayi:",min(sayilar))

sayilar=sayilari_al()
analiz_et(sayilar)




    
