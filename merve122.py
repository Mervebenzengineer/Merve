#Alper Akbas Notlari

#ENCAPSULATION,KAPSULLEME,PRIVATE VE PUBLIC DEGISKENLER

class Personel:

    def __init__(self,isim,soyisim,maas):
        self.isim=isim #Global deger
        self.soyisim=soyisim
        self.maas=maas
        self.__zam_orani=1.05 #Private

    def getZamOrani(self):
        return self.__zam_orani

    def setZamOrani(self,oran):
        self.__zam_orani=oran 

    def zam_uygula(self):
        self.maas=int(self.maas*self.__zam_orani)



per_1=Personel('Dean','Winchester',10000)


print(per_1.getZamOrani())




