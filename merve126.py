#Property Decorators,getters,setters,deleters

class Personel:
    zam_orani=1.05

    def __init__(self,isim,soyisim,maas):
        self.isim=isim
        self.soyisim=soyisim
        self.maas=maas

    @property
    def eposta(self):
        return f'{self.isim}.{self.soyisim}@firmam.com'

    @property
    def tam_isim(self):
        return f'{self.isim} {self.soyisim}'
    
    @tam_isim.setter
    def tam_isim(self,ad):
        isim,soyisim=ad.split(' ')
        self.isim=isim
        self.soyisim=soyisim

    @tam_isim.deleter
    def tam_isim(self):
        print('DEGISKENLER SILINDI!')
        self.isim=None
        self.soyisim=None


per_1=Personel('Dean','Winchester',10000)

per_1.tam_isim = 'Merve ASO'
print(per_1.isim)
print(per_1.eposta)
print(per_1.tam_isim)

del per_1.tam_isim
print(per_1.isim)
