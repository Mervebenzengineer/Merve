#np.unique
#np.sort()

import numpy as np

veriler=np.array([5,2,7,2,9,5,7])
benzersiz=np.unique(veriler)
print("Benzersiz elemanlar:",benzersiz)

sirali=np.sort(veriler)
print("Sirali\n",sirali)

indeksler=np.argsort(veriler)
print("Siralama indeksleri:\n",indeksler)
print("Bu indekslere gore sirali veri:",veriler[indeksler])

sinirli=np.clip(veriler,0,5)
print("0-5 araligina sıkıstırılmıs veri\n",sinirli)

"""
np.unique
Amacı: Tekrarlayan elemanları kaldırır, benzersiz olanları döndürür.
Kullanım Alanı: Veri temizleme, aynı değeri birden fazla saymamak istediğimiz durumlar.
"""

"""
np.sort()
Amacı: Diziyi sıralı şekilde döndürür. (Orijinal diziyi değiştirmez, yeni bir kopya döner.)
Kullanım Alanı: Küçükten büyüğe ya da büyükten küçüğe sıralama.
"""

"""
np.argsort()
Amacı: Diziyi sıralamak için indeks sırasını verir.
Kullanım Alanı: Sıralama sonrası orijinal verinin hangi indekslerde olduğunu bulmak.
"""

"""
np.clip()
Amacı: Belirlenen aralık dışındaki değerleri sınırlar.
Kullanım Alanı: Not, sıcaklık, puan gibi verilerde minimum-maksimum değer aralığını korumak.
"""