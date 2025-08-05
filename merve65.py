import pandas as pd 
import matplotlib.pyplot as plt
veri={
    "Isim":["Merve","can","a"],
    "not":[90,86,78],
    "yas":[23,34,18]
}
df=pd.DataFrame(veri)#excel dosyasi olusur.sozlukten tablo oluusur.
print(df)

df=pd.DataFrame(veri)

ortalama=df["not"].mean()#df["not"] notlari alir .mean ort alir.
df["ortalama"]=ortalama*len(df)

en_yuksek=df["not"].max()
en_dusuk=df["not"].min()

print("Tablo:\n",df)
print("\nEn yuksek not:",en_yuksek)
print("En dusuk not:",en_dusuk)

#df.to_csv("Ogrenciler.csv",index=False)
#print("\nVeriler CSV dosyasina kaydedildi.")

#df_yeni=pd.read_csv("Ogrenciler.csv")
#print("\nCSV'den okunan tablo:",df_yeni)

#plt.bar(df["Isim"],df["not"],color="orchid")

#plt.title("Ogrenci Notlari")
#plt.xlabel("Isimler")
#plt.ylabel("Notlar")
#plt.ylim(0,100)
#plt.tight_layout()

#plt.show()

plt.pie(df["not"],labels=df["Isim"],colors=["red","blue","green"],autopct="%1.1f%%",startangle=90)
plt.title("Ogrenci notlari")
plt.axis("equal")
plt.show()