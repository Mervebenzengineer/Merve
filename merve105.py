#np.concatenate()
# Veri setlerini birleştirme, ek satır/kolon ekleme.

import numpy as np

a=np.array([[1,2],[3,4]])

b=np.arrat([[5,6],[7,8]])

sonuc=np.concatenate((a,b),axis=0)
print("Alt alta birlestirme:\n",sonuc)

sonuc2=np.concatenate((a,b),axis=1)
print("Yan yana birlestirme:\n",sonuc2)

