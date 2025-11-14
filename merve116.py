#ENCAPSULATION (KAPSÜLLEME)

"""
Verileri korumak için doğrudan erişimi engelleme.
__degisken → Özel değişken (dışarıdan doğrudan erişilemez).
@property → Getter (okuma), @<isim>.setter → Setter (yazma) ile kontrol."""


class Arac:
    def __init__(self,marka,model,yil,km):
        self.marka=marka
        self.model=model
        self.yil=yil
        self.__km=km # Özel değişken

    @property
    def km(self):
        return self.__km
    
    @km.setter
    def km(self,yeni_km):
        if yeni_km<self.__km:
            raise ValueError("KM geri alinamaz")
        self.__km=yeni_km


araba=Arac("BMW","320i",2020,5000)
print(araba.km)
araba.km=5500
print(araba.km)


        

