#Kalitim

class Personel:
    personel_sayisi=0
    zam_orani=1.05

    def __init__(self,isim,soyisim,maas):
        self.isim=isim
        self.soyisim=soyisim
        self.maas=maas
        self.eposta=f'{isim.lower()}.{soyisim.lower()}@firmam.com'
        #print(f"Yeni personel tanimlandi:{isim} {soyisim}")

    def tam_isim(self):
        return f'{self.isim} {self.  soyisim}'
    

    def zam_uygula(self):
        self.maas=int(self.maas*Personel.zam_orani)

##METHOD RESOLUTION ORDER
class Yazilimci(Personel):
    zam_orani=1.1
    def __init__(self,isim,soyisim,maas,prog_dil):
        super().__init__(isim,soyisim,maas)
        
        self.prog_dil=prog_dil
        #print(f"Yeni personel yazilimci kategorisine tasindi:{self.isim} {self.soyisim}")

class Mudur(Personel):
    def __init__(self,isim,soyisim,maas,personeller=None):
        super().__init__(isim,soyisim,maas)
        if personeller is None:
            self.personeller=[]
        else:
            self.personeller=personeller
    
    def personel_ekle(self,per):
        if per not in self.personeller:
            self.personeller.append(per)

    
    def personel_cikar(self,per):
        if per in self.personeller:
            self.personeller.remove(per)


    def personelleri_listele(self):
        for e, per in enumerate(self.personeller):
            e+=1
            print(e,per.tam_isim())



 
yaz_1= Yazilimci('Dear','Smith',30000,'python')
yaz_2=Yazilimci('Mary','Smith',35000,'java')

mdr_1=Mudur('John','Wick',50000,[yaz_1])

print(mdr_1.tam_isim())
print("____________")
mdr_1.personelleri_listele()
print("____________")
mdr_1.personel_ekle(yaz_2)
mdr_1.personel_cikar (yaz_1)
mdr_1.personelleri_listele()






 







 