#Histogram Grafigi

import matplotlib.pyplot as plt

notlar=[45,60,70,85,90,90,60,55,100,75,70,60,85,95]

plt.hist(notlar,bins=5,color="red",edgecolor="black")

plt.title("Sinav Notlari Histogrami")
plt.xlabel("Not Araliklari")
plt.ylabel("Ogrenci Sayilari")

plt.grid(True)
plt.show()