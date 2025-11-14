#np.split()
import numpy as np

dizi = np.arange(10)  # 0'dan 9'a kadar
print("Orijinal:", dizi)

parcalar = np.split(dizi, 5)  # 5 eşit parçaya böl
print("Parçalar:", parcalar)

"""Diziyi eşit parçalara ayırır.
#İkinci parametre → kaç parçaya bölüneceğini belirtir.
Bölünecek uzunluk, parçaya tam bölünebilir olmalı yoksa hata verir.
"""
