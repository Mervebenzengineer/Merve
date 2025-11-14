#Polymorhism(Çok Biçimcilik)
#Aynı isimli metotların farklı sınıflarda farklı çalışması.


# Temel sınıf (Parent Class)
class Arac:
    # self: oluşturulan her nesneyi temsil eder (C'deki pointer gibi düşünülebilir)
    # __init__ : yapıcı metod (constructor). Nesne oluşturulduğunda otomatik çalışır.
    def __init__(self, marka, model):
        self.marka = marka   # Nesneye özel marka bilgisi
        self.model = model   # Nesneye özel model bilgisi

    # Bu metot tüm araçlar için geçerli, ama alt sınıflarda (child class) değiştirilebilir
    def calistir(self):
        print("Araç çalıştırıldı.")


# Araba sınıfı, Arac sınıfından miras alıyor (inheritance)
class Araba(Arac):
    # Burada __init__ yeniden yazmaya gerek yok, parent class'dan miras geliyor
    def calistir(self):  
        # Aynı isimli metodu farklı şekilde tanımladık → Polymorphism
        print(f"{self.marka} marka araba motoru çalıştı.")


# Motorsiklet sınıfı, yine Arac sınıfından türedi
class Motorsiklet(Arac):
    def calistir(self):
        print(f"{self.marka} marka motorsiklet motoru çalıştı.")


# Otobüs sınıfı da aynı şekilde Arac sınıfından türedi
class Otobus(Arac):
    def calistir(self):
        print(f"{self.marka} marka otobüs motoru çalıştı.")


# Burada farklı tipte araç nesneleri oluşturuyoruz
araclar = [
    Araba("Mercedes", "C200"),
    Motorsiklet("Yamaha", "R25"),
    Otobus("Mercedes", "Travego")
]

# Döngü ile tüm araçları çalıştırıyoruz
# Polymorphism sayesinde aynı isimli 'calistir()' metodu
# her sınıfta farklı çalışıyor!
for arac in araclar:
    arac.calistir()
