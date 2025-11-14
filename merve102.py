#NumPy Ileri seviye fonksiyonlari

import numpy as np
"""
dizi=np.arange(12)
print(dizi)

yeni=dizi.reshape(3,4)#3 satir 4 sütun 
print(yeni)
"""

notlar=np.random.randint(0,101,size=40)
print("Tek boyutlu nit listesi:\n",notlar)

not_tablosu=notlar.reshape(8,5)
print("\n8 ogrenci × 5 derslik not tablosu:\n",not_tablosu)

print("\nHer dersin ortalamasi:",np.mean(not_tablosu,axis=0))

print("Her ogrencinin ortalamasi:",np.mean(not_tablosu,axis=1))

