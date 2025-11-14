#np.hsplit()

import numpy as np

matris = np.arange(16).reshape(4, 4)
print("Matris:\n", matris)

parcalar = np.hsplit(matris, 2)  # 2 sütuna böl
print("Yatay parçalar:", parcalar)


#Sütunlardan (yan yana) bölme yapar.
#CSV’de kolonları ayırma gibi düşünebilirsin