#Encapsulation (Kapsülleme)
"""

Bir sınıfın içindeki verilerin (özelliklerin/atribütlerin) dışarıdan doğrudan erişilmesini engelleyip, sadece sınıfın metodları üzerinden kontrollü şekilde erişilmesine kapsülleme denir.
➡️ Yani: Veriyi gizler, gerektiğinde sadece belirlenen kapılardan (get/set metodları gibi) dışarı açar."""


#Normal Durum (korumasız erişim)

class Arac:
    def __init__(self,marka,hiz):
        self.marka=marka
        self.hiz=hiz

araba=Arac("Mercedes",220)
print(araba.hiz)
