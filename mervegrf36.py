#Bar (Cubuk) Grafigi
import matplotlib.pyplot as plt
dersler=["Matematik","Fizik","Kimya"]
puanlar=[80,65,90]
plt.bar(dersler,puanlar)

plt.title("Derslere gore puan dagilim")
plt.xlabel("Dersler")
plt.ylabel("Puanlar")
plt.show()