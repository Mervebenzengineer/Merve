def sayi_al():
    liste=[]
    while True:
        veri=input("Sayi girin(cikmak icin'q'):")
        if veri=="q":
            print("Girdi islemi sona erdi.\n")
            break
        try:
            sayi=float(veri)
            liste.append(sayi)
        except ValueError:
            print("Gecerli sayi girin")
        return liste
def toplam(liste):
    return sum(liste)
def ortalama(liste):
    return sum(liste)/len(liste)
def en_buyuk(liste):
    return max(liste)
def en_kucuk(liste):
    return min(liste)
def analiz_et():
   sayilar=sayi_al()
   if not sayilar:
       print("Hic sayi girilmedi")
       return
   print("Sayi analizi:")
   print("Toplam:",toplam(sayilar))
   print("Ortalama:",ortalama(sayilar))
   print("En buyuk:",en_buyuk(sayilar))
   print("En kucuK:",en_kucuk(sayilar))



