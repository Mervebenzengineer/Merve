#self olusturulan siniftaki nesneleri ifade eder
#
class Personel:
    personel_sayisi=0
    zam_orani=1.05

    def __init__(self,isim,soyisim,maas):
        self.isim=isim
        self.soyisim=soyisim
        self.maas=maas
        self.eposta=f'{isim.lower()}.{soyisim.lower()}@firmam.com'
        Personel.personel_sayisi+=1
        



    def tam_isim(self):
        return f'{self.isim} {self.  soyisim}'
    

    def zam_uygula(self):
        self.maas=int(self.maas*Personel.zam_orani)

    @classmethod
    def zam_oranini_belirle(cls,oran):
       eski_oran=cls.zam_orani
       cls.zam_orani=oran

       print(f'Eski zam orani ({eski_oran}) guncellendi.Yeni oran:{cls.zam_orani}')
    @classmethod
    def from_string(cls,per_str):
        isim,soyisim,maas=per_str.split('-')
        return cls(isim,soyisim,maas)
    
    @staticmethod
    def mesai_gunu(gun):
        if gun.weekday()== 5 or gun.weekday()==6:
            return 'Hafta Sonu'
        else:
            return 'Hafta Ici'
    


per_1= Personel('John','Smith',30000)
per_2=Personel('Mary','Smith','35000')
 

per_str_1='Sam-Winchester-40000'
per_str_2='Dean-Winchester-60000'
per_str_3='Bobby-Singer-60000'

yeni_per_1=Personel.from_string(per_str_2)

print(yeni_per_1.eposta)
print(yeni_per_1.maas)

 
