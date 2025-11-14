import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[2,4,6,8,10]
plt.plot(x,y,color="green",linestyle="--",marker="o",label="2x") #cizgi grafigi olusturur

plt.title("Stil Verilmis Cizgi Grafigi")
plt.xlabel("x Ekseni")
plt.ylabel("y ekseni")

plt.grid(True)
plt.legend()
plt.show()

