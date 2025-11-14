#INHERİTANCE(Kalitim)
"""Bir sınıfın özelliklerini ve metotlarını başka bir sınıfa aktarmaktır.
Temel sınıf (Base / Parent) → Ortak özellikler burada.
Alt sınıf (Child / Subclass) → Temel sınıftan miras alır, kendi ek özelliklerini ekleyebilir.
"""

class Arac:
    def __init__(self, marka, model, yil):
        self.marka = marka
        self.model = model
        self.yil = yil

    def bilgi(self):
        print(f"{self.marka} {self.model} ({self.yil})")

class BenzinliArac(Arac):
    def __init__(self, marka, model, yil, depo_litre):
        super().__init__(marka, model, yil)  # Üst sınıfın __init__'ini çağırıyoruz
        self.depo_litre = depo_litre

class ElektrikliArac(Arac):
    def __init__(self, marka, model, yil, batarya_kwh):
        super().__init__(marka, model, yil)
        self.batarya_kwh = batarya_kwh

araba1 = BenzinliArac("Mercedes", "C200", 2018, 55)
araba2 = ElektrikliArac("Tesla", "Model 3", 2022, 75)

araba1.bilgi()
araba2.bilgi()
