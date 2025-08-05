import random
sayi=random.randint(1,10)
tahmin=-1
print("1 ile 10 arasinda sayi tuttum.Tahmin etmeye calis")
while tahmin!=sayi:
    tahmin=int(input("Tahminin:"))
if tahmin<sayi:
    print("Daha buyuk bir sayi dene!")
elif tahmin>sayi:
    print("Daha kucuk bir sayi denemelisin")
else:
    print("Tebrikler!Dogru tahmin")

