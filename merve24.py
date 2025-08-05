liste=[]
print("Sayi girin.Cikmak icin 'q' yazin")

while True:
    veri=input("Sayi:")
    if veri=="q":
        print("Dongu sonlandirildi")
        break
    try:
        sayi=float(veri)
        liste.append(sayi)
    except ValueError:
        print("Gecerli sayi girin")

print("Girilen sayi adedi",len(liste))
print("Sayilarin toplami:",sum(liste))
print("En buyuk sayi:",max(liste))
print("En kucuk sayi:",min(liste))
ortalama=sum(liste) / len(liste)
print("Ortalama:",ortalama)
    




