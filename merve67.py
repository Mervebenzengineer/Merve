import pandas as pd
ogrenciler={
    "O1":{"isim":"Merve","not":90,"yasi":23},
    "O2":{"isim":"Ali","not":85,"yasi":20},
    "O3":{"isim":"Can","not":100,"yasi":24}
}
df=pd.DataFrame(ogrenciler).T
print(df)

print("\n85'ten buyuk notlar:")
print(df[df["not"]>=85])

print("\nYasi 20'den buyuk olanlar:")
print(df[df["yasi"]>20])

print(df.sort_values("not"))
print(df.sort_values("yasi"))

ortalama=df["not"].mean()
print("Ortalama Not:",ortalama)


en_yuksek=df["not"].max()
en_dusuk=df["not"].min()

print("En yuksek not:",en_yuksek)
print("En dusuk not:",en_dusuk)

df.to_csv("ogrenciler.csv",index=False)
print("\nBilgiler disa aktarildi")




