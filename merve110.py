#np.vsplit()
import numpy as np

matris=np.arange(16).reshape(4,4)
print("Matris:\n",matris)

parcalar=np.vsplit(matris,2)
print("Dikey parcalar:",parcalar)

"""
Satırlardan (alt alta) bölme yapar.
Veri setini gruplara ayırmada kullanılır.
"""