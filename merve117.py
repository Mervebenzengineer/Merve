#CLASSMETHOD(SINIF DEGISKENLERI)

"""Sınıf değişkeni: Tüm nesneler için ortak olan değişken.
@classmethod → Sınıf düzeyinde işlem yapmak için.
"""

class Arac:
    toplam_arac=0

    def __init__(self,marka):
        self.marka=marka
        Arac.toplam_arac+=1

    @classmethod
    def sayi_goster(cls):
        print(f"Toplam arac sayisi:{cls.toplam_arac}")

araba1=Arac("Mercedes")
araba2=Arac("BMW")
Arac.sayi_goster()


