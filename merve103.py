#ravel()
import numpy as np

dizi=np.array([[1,2,3],[4,5,6]])

tek_boyut=dizi.ravel()
print("ravel sonucu:",tek_boyut)

tek_boyut[0]=99
print("\nOrijinal dizi:\n",dizi)

