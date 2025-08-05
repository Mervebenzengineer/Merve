#Temel Bar Grafigi
import matplotlib.pyplot as plt 

gunler=["Pazartesi","Sali","Carsamba"]
satislar=[120,150,180]

plt.bar(gunler,satislar,color="red")
plt.title("Haftalik Satis Grafigi")
plt.xlabel("Gunler")
plt.ylabel("Satis Miktari")
plt.grid(axis="y")
plt.show()