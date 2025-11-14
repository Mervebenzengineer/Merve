import numpy as np

dizi1 = np.random.randint(0, 99, size=(10,))
dizi2 = np.random.randint(0, 10, size=(5,))
dizi3 = np.random.randint(89, 99, size=(3,))
dizi4 = np.random.randint(0, 99, size=(5,))

print("Dizi1:", dizi1)
print("Dizi2:", dizi2)
print("Dizi3:", dizi3)
print("Dizi4:", dizi4)

print("Dizi1 boyut sayısı (ndim):", dizi1.ndim)
print("Dizi1 şekli (shape):", dizi1.shape)
print("Dizi1 veri tipi (dtype):", dizi1.dtype)

dizi1_float = dizi1.astype(float)
print("Float versiyonu:", dizi1_float)
