import matplotlib.pyplot as plt
ogrenciler={}
dersler=["A","B","C"]

for i in range(3):
    ad=input(f"Ogrenci {i+1} adi girin:")
    notlar=[]
    for ders in dersler:
        while True:
            try: 
                puan=float(input(f"{ad}-{ders} notu girin"))
            
                if 0<=puan<=100:
                    notlar.append(puan)
                    break
                else:
                    print("Gecerli not girin")
            except ValueError:
                print("Gecerli puan girin")
        ogrenciler[ad]=notlar
for isim,notlar in ogrenciler.items():
   ort=sum(notlar)/len(notlar)
   ogrenciler[isim].append(ort)
   
isimler=list(ogrenciler.keys())
ortalamalar=[ogrenciler[isim][3] for isim in ogrenciler]

plt.bar(isimler,ortalamalar,color="red")
plt.title("Not ortalamalari")
plt.xlabel("Ogrenciler")
plt.ylabel("Ortalamalar")
plt.ylim(0,100)
plt.tight_layout()
plt.savefig("notgrafigi_png")
plt.show()

with open("notgrafigi.png","r") as dosya:
    icerik=dosya.read()
    print(icerik)
    input("Cikmak icin entere basin")
    exit()
  









  



