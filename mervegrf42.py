import matplotlib.pyplot as plt
import numpy as np

gunler=["Pzt","Sal","Car"]
urunA=[120,150,180]
urunB=[100,130,80]

x=np.arange(len(gunler))

plt.bar(x-0.2,urunA,width=0.4,label="Urun A", color="green")

plt.bar(x+0.2,urunB,width=0.4,label="Urun B",color="purple")

plt.xticks(x,gunler)

plt.title("Urun Satis Karsilastirmasi")
plt.xlabel("Gunler")
plt.ylabel("Satis Adedi")
plt.legend()
plt.grid(axis="y")
plt.show()