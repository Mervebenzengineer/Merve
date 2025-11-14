#Kapsulleneme ile  Gizleme

#Python’da bir özelliği “özel” yapmak için başına çift alt çizgi (__) koyarız.


class Arac:
    def __init__(self, marka, hiz):
        self.marka = marka
        self.__hiz = hiz   # özel özellik (dışarıdan ulaşılamaz)

    # Getter metodu (okuma için)
    def get_hiz(self):
        return self.__hiz
    
    # Setter metodu (güncelleme için, kontrollü)
    def set_hiz(self, yeni_hiz):
        if yeni_hiz > 0:  # kontrol şartı
            self.__hiz = yeni_hiz
        else:
            print("Hız 0'dan küçük olamaz!")

araba = Arac("BMW", 180)

# Doğrudan erişim hata verir
# print(araba.__hiz) ❌

# Getter ile okuma
print("Arabanın hızı:", araba.get_hiz())

# Setter ile değiştirme
araba.set_hiz(200)
print("Yeni hız:", araba.get_hiz())
