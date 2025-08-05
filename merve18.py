import random
sayi=random.randint(1,100)
tahmin=-1
deneme=0
print("1 ile 100 arasinda sayi tuttum.Tahmin et!")
while tahmin!=sayi:
    tahmin=int(input("Tahminin nedir?"))
    deneme+=1
    if tahmin<sayi:
        print("Daha buyuk sayi soyle!")
    elif tahmin>sayi:
        print("Daha kucuk sayi soyle")
    else:
        print(f"Tebrikler!{deneme}denemede bildin")
