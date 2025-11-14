import random
sayi=random.randint(1,100)
tahmin=-1
deneme=0
hak=7

print("1,100 arasinda sayi tuttum tahmin et?")

while tahmin!=sayi and deneme<hak:
    tahmin=int(input("Tahmininiz nedir?"))
    deneme+=1
    
    if tahmin<sayi:
        print("Daha buyuk bir sayi soyle!")
        
    elif tahmin>sayi:
        print("Daha kucuk sayi soyle")

    else:
       print("Tebrikler {deneme}.denemede dogru bildin")
       
if tahmin!=sayi:
    print("Maalesef kaybettiniz.Dogru sayi{sayi}")
       




