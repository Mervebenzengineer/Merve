import numpy as np

dizi=np.random.randint(0,100,size=(20,5))

toplam=dizi.sum()
print(toplam)

toplam_sutun=dizi.sum(axis=0)
print("\n",toplam_sutun)

toplam_satir=dizi.sum(axis=1)
print("\n",toplam_satir)

scores=dizi
idx=np.where(scores>75)
print(idx)
print(scores[idx])



