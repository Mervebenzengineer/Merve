#flatten()
import numpy as np
dizi=np.array([[1,2,3],[4,5,6]])

tek_boyut=dizi.flatten()
print("Flatten sonucu:",tek_boyut)

tek_boyut[0]=99
print("Orijinal dizi:\n",dizi)


#flatten() her zaman yeni bir kopya döndürür.(tek boyutlu hale gelir)
#Yeni dizide yapılan değişiklikler orijinal diziyi etkilemez.