import numpy as np

notlar = np.array([105, 95, 75, -5, 60, 75, 200])

# 1- Benzersiz değerler
print("Benzersiz:", np.unique(notlar))

# 2- Sıralama
print("Sıralı:", np.sort(notlar))

# 3- Sıralama indeksleri
print("Sıralama indeksleri:", np.argsort(notlar))

# 4- 0–100 aralığına sıkıştırma
print("0-100 aralığına sıkıştırılmış:", np.clip(notlar, 0, 100))


