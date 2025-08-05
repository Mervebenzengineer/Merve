#Stil ve Tick'larla Grafik

import matplotlib.pyplot as plt 
import numpy as np

x=np.arange(0,11,1)
y=2*x

plt.plot(x,y,color="green",linestyle="--",marker="o",label="y=2x")

plt.title("2x Fonksiyonu Grafigi")
plt.xlabel("X Ekseni")
plt.ylabel("Y Ekseni")

plt.xticks(np.arange(0,11,1))
plt.yticks(np.arange(0,21,2))

plt.grid(True)
plt.legend()
