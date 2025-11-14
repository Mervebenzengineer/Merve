#Magic (Dunder) Methods
"""Python’daki özel işlevlerdir.
Adlarının başında ve sonunda çift alt çizgi (__) bulunur.
Normalde biz çağırmadan otomatik çalışırlar.
"""


class Arac:
    # __init__ => Nesne oluşturulurken otomatik çalışan yapıcı (constructor) metot
    # Burada markayı, modeli ve yılı her nesneye özgü saklıyoruz.
    def __init__(self, marka, model, yil):
        self.marka = marka   # self => her nesneye ait veriyi saklar
        self.model = model
        self.yil = yil
    
    # __str__ => print() ile nesneyi yazdırmak istediğimizde çalışır
    # Normalde "object at 0x..." gibi bir çıktı alırdık, bunu daha anlamlı hale getiriyoruz
    def __str__(self):
        return f"{self.marka} {self.model} ({self.yil})"
    
    # __len__ => len(nesne) çağırıldığında çalışır
    # Burada markanın ve modelin toplam uzunluğunu (karakter sayısı) döndürüyoruz
    def __len__(self):
        return len(self.marka + self.model)
    
    # __add__ => + operatörünü iki nesne arasında kullanmak istediğimizde çalışır
    # İki aracın marka adını birleştirip özel bir çıktı veriyoruz
    def __add__(self, other):
        return f"{self.marka} & {other.marka} işbirliği!"

# Nesne oluşturma aşaması
# __init__ otomatik çalışıyor ve her nesne kendi verilerini alıyor

a1 = Arac("Mercedes", "C200", 2020)
a2 = Arac("BMW", "320i", 2021)

# __str__ çalışır → print(a1) dediğimizde __str__ metodu devreye giriyor
print(a1)  

# __len__ çalışır → len(a1) dediğimizde __len__ metodu devreye giriyor
print(len(a1))  

# __add__ çalışır → a1 + a2 dediğimizde __add__ metodu devreye giriyor
print(a1 + a2)
