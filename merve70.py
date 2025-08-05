import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("Ogrenciler.csv")

print("Ogrenci Veriler:")
print(df)

ortalama=df["not"].mean()
print("\nOrtalama Not:",ortalama)

print("En yuksek not:",df["not"].max())
print("En dusuk not:",df["not"].min())

basarisizlar=df[df["not"]<60]
print("\nBasarisiz Ogrenciler:")
print(basarisizlar)

plt.bar(df["isim"],df["not"],color="skyblue")
plt.title("Ogrencilerin Notlari")
plt.xlabel("Isimler")
plt.ylabel("Notlar")
plt.ylim(0,100)
plt.grid(True)
plt.show() 