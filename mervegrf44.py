#Pasta Grafigi (Pie Chart)

import matplotlib.pyplot as plt 

diller=["Python","C#","Java"]
oranlar=[45,30,25]
renkler=["lightgreen","skyblue","lightcoral"]

plt.pie(oranlar,labels=diller,colors=renkler,autopct="%1.1f%%",startangle=90)
plt.title("Proglama Dilleri Dagilimi")
plt.axis("equal")

plt.show()