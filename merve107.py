#np.hstack()

import numpy as np

a=np.array([1,2,3])
b=np.array([4,5,6])

sonuc=np.hstack((a,b))
print("hstack sonucu:\n",sonuc)
"""
hstack → dizileri yan yana ekler.
axis=1 kullanımına benzer.
"""