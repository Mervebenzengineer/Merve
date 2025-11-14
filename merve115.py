#OVERRIDING(METOT EZME)
"""
Alt sınıf, üst sınıfta var olan bir metodu kendi ihtiyacına göre değiştirir.
super() → Üst sınıftaki orijinal metodu çağırmak için kullanılır.
"""
class Arac:
    def calistir(self):
        print("[Arac] Calistiriliyor...")

class BenzinliArac(Arac):
    def calistir(self):
        super().calistir() # Üst sınıfın metodu da çalışsın

        print("[Benzinli] Motor sesi ile calisti.")

class ElektrikliArac(Arac):
    def calistir(self):
        print("[Elektrikli] Sessiz modda calisti.")
        

araba1=BenzinliArac()
araba2=ElektrikliArac()

araba1.calistir()
araba2.calistir()

