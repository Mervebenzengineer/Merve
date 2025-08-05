import matplotlib.pyplot as plt

x=[1,2,3,4,5]
y1=[i**2 for i in x]
y2=[i*2 for i in x]
y3=[10-i for i in x]
y4=[i%2 for i in x]

plt.subplot(2,2,1)
plt.plot(x,y1)
plt.title("Kareleri")

plt.subplot(2,2,2)
plt.plot(x,y2)
plt.title("Carpimlari")

plt.subplot(2,2,3)
plt.plot(x,y3)
plt.title("Azalan Degeri")

plt.subplot(2,2,4)
plt.plot(x,y4)
plt.title("Modu")

plt.tight_layout()
plt.show()
