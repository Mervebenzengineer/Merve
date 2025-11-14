def topla(a,b):
    return a+b
def cikar(a,b):
    return a-b
def carp(a,b):
    return a*b
def bol(a,b):
    return a/b

sayi1=float(input("Birinci sayiyi girin:"))
sayi2=float(input("Ikinci sayiyi girin:"))

print("Hangi islemi yapmak istersin?")
print("1.Toplama:")
print("2.Cikarma")
print("3.Carpma")
print("4.Carpma")
secim=input("Seciminiz(1-2-3-4):")

if secim=="1":
    sonuc=topla(sayi1,sayi2)
elif secim=="2":
    sonuc=cikar(sayi1,sayi2)
elif secim=="3":
    sonuc=carp(sayi1,sayi2)
elif secim=="4":
    sonuc=bol(sayi1,sayi2)
else:
    print("Gecersiz secim!")
    exit()
print(f"Sonuc:{sonuc}")


            
    