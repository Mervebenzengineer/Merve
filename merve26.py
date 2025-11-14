import random
toplam=0
sayac=0
      
while toplam<100:
   sayi=random.randint(1,10)
   toplam+=sayi
   sayac+=1
   print(f"{sayac}.sayi:{sayi}")
   print(f"Toplam:{toplam}")
   
print(f"Oyun bitti!{sayac} adimda 100'u gectiniz.")
    


