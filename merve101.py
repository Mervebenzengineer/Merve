import numpy as np

dizi=np.random.randint(0,100,size=(10,5))

ortalama=np.mean(dizi)
print("Ortalama degeri:",ortalama)

ortada=np.median(dizi)
print("Ortadaki sayi:",ortada)

sp=np.std(dizi)
print("Standart sapma degeri:",sp)

vr=np.var(dizi)
print("Varyans degeri:",vr)

toplam_sutun=dizi.sum(axis=0)
print("\nSutun degeri:",toplam_sutun)

toplam_satir=dizi.sum(axis=1)
print("\nSatir degeri:",toplam_satir)

