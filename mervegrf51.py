import matplotlib.pyplot as plt

x=[1,2,3,4,5]
y=[2,4,6,8,10]

plt.subplot(2,2,1)
plt.plot(x,y,color="blue")
plt.title("Cizgi Grafigi")

plt.subplot(2,2,2)
plt.bar(x,y,color="orange")
plt.title("Bar Grafigi")

plt.subplot(2,2,3)
plt.scatter(x,y,color="green")
plt.title("Nokta Grafigi")

plt.subplot(2,2,4)
etiketler=["A","B","C","D","E"]
plt.pie(y,labels=etiketler,autopct="%1.1f%%",startangle=90)
plt.title("Pasta Grafigi")

plt.tight_layout()
plt.show()