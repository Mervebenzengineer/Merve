#for i in range(2,11,2):
 
#print("Cift sayilar",i)

isimler=[]#liste olusturma
for i in range(5):#dongu 5 doner
    isim=input(f"{i+1}.ismi girin")#isimalinir
    isimler.append(isim)#girilen isimler listeseye yazilir
print("\nGirdiginiz isimler:")
for isim in isimler:
    print(isim)


