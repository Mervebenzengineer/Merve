import pandas as pd
import matplotlib.pyplot as plt 
merve={
    "Ogrenci1":{"isim":"A","numara":2345,"not":78,"yas":21},
    "Ogrenci2":{"isim":"B","numara":2445,"not":79,"yas":20},
    "Ogrenci3":{"isim":"C","numara":2545,"not":80,"yas":23}
}
df=pd.DataFrame(merve).T

ortalama=df["not"].mean()
print("Ortalama not",ortalama)

en_yuksek=df["not"].max()
print("En yuksek not:",en_yuksek)

en_dusuk=df["not"].min()
print("En dusuk not:",en_dusuk)

print(df[df["not"]<85])
print(df[df["yas"]<22])

df.to_csv("merve.csv",index=False)
print("\nBilgiler disa aktarildi.")

df_yeni=pd.read_csv("merve.csv")
print("\nDosyadan okunana veriler:")

print(df_yeni)

plt.bar(df["isim"],df["not"],color="yellow")
plt.title("Ogrenciler ve Notlari")
plt.xlabel("isimler")
plt.ylabel("Notlar")
plt.ylim(0,100)
plt.show()
