import matplotlib.pyplot as plt 
x=[1,2,3]
y=[1,4,9]
plt.plot(x,y,label="y=x",color="blue",linestyle="-",marker="o")
plt.title("Cizgi Grafigi:y=x kare")
plt.xlabel("x ekseni")
plt.ylabel("y ekseni")
plt.grid(True)
plt.legend()
plt.show()
