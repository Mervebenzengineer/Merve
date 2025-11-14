import random
toplam=0
sayac=0
sayilar=[]

while toplam<100:
    sayi=random.randint(1,10)
    toplam+=sayi
    sayac+=1
    sayilar.append(sayi)
    print(f"{sayac}.sayi:{sayi}")
    print(f"toplam:{toplam}")
    
print("Oyun bitti!")
print("Tum sayilar:",sayilar)
print("En buyuk sayi:",max(sayilar))
print("Ortalama:",sum(sayilar)/len(sayilar))
    
