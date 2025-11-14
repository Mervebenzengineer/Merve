#dunder method

class Personel:
    zam_orani=1.05
    def __init__(self,isim,soyisim,maas):
        self.isim=isim
        self.soyisim=soyisim
        self.maas=maas
        self.eposta=f'{isim.lower()}.{soyisim.lower()}@firmam.com'


    def tam_isim(self):
        return f'{self.isim} {self.soyisim}'
    
    def zam_uygula(self):
        self.maas=int(self.maas*self.zam_orani)

    def __repr(self):
        return f"Personel ('{self.isim}','{self.soyisim}','{self.maas}')"
     

    def __add__(self,other):
        return self.maas+other.maas
    
    def __len__(self):
        return len(self.tam_isim())
    



per_1=Personel('Dean','Winchester',10000)
per_2=Personel('Sam','Winchester',15000)

print(per_1+per_2)
"""
print(per_1__add__(per_2))
print(Personel.__add__(per_1,per_2))
31ve 32. yorum satiri 29.satirla ayni ciktiyi verir.
"""

print(len(per_1))






      