#subplot

import matplotlib.pyplot as plt

x=[1,2,3,4,5]
y1=[1,4,9,16,25]
y2=[25,20,15,10,5]

#ilk grafik:cizgi grafigi
plt.subplot(1,2,1)
plt.plot(x,y1)
plt.title("Artan Degerler")

#ikinci grafigi:cubuk grafigi
plt.subplot(1,2,2)
plt.bar(x,y2)
plt.title("Azalan Degerler")

plt.tight_layout() #Grafik ust uste binmesin

plt.show()
