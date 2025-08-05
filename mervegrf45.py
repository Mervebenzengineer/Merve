import matplotlib.pyplot as plt
diller=["Python","Java","JavaScript"]
kullanim=[45,30,25]

plt.bar(diller,kullanim,color="skyblue")

plt.title("Programlama Dillerinin Kullanim Orani")
plt.xlabel("Diller")
plt.ylabel("Kullanim(%)")

plt.show()