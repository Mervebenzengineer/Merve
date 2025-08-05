import matplotlib.pyplot as pyt

x=[1,2,3]
y1=[1,4,9]
y2=[30,20,10]

pyt.subplot(1,2,1)
pyt.plot(x,y1)
pyt.title("Artan Degerler")

pyt.subplot(1,2,2)
pyt.plot(x,y2)
pyt.title("Azalan Degerler")

pyt.tight_layout()
pyt.show()

