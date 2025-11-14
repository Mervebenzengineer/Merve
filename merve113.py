#OOP
class Arac:
    def __init__(self,marka,model,renk,yil):
        self.marka=marka
        self.model=model
        self.renk=renk
        self.yil=yil 

    def bilgi_goster(self):
        print(f"Araba markasi:{self.marka},Modeli:{self.model},Rengi:{self.renk},Yili:{self.yil}\n")


    def calistir(self):
        print(f"{self.marka} Calistirildi.\n")

araclar= [

Arac("Mercedes","2016","Beyaz",2016),

Arac("BMW","2020","Beyaz",2020),

Arac("Porche","2019","Beyaz",2019),

Arac("Chery","2018","Beyaz",2018)
]


for Arac in araclar:
    Arac.bilgi_goster()
    Arac.calistir()
