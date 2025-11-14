#np.vstack()
import numpy as np

a=np.array([1,2,3])
b=np.array([4,5,6])

sonuc=np.vstack((a,b))
print("vstack sonucu:\n",sonuc)

"""
vstack → dizileri alt alta ekler.
axis=0 kullanımına benzer, ama daha okunaklı.
"""