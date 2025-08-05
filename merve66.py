import pandas as pd
veri={
    "Isim":["Merve","A","B"],
    "Not":[90,75,85],
    "Yas":[23,21,24]
}
df=pd.DataFrame(veri)
print(df)
#filtreleme
print(df[df["Not"]>=85])#Notu 85 ve ustu olan ogrenciler
print(df[df["Not"]>=85])& (df["Yas"]==23)

#siralama
print(df.sort_values("Not"))#k->b
print(df.sort_values("Not"))#b->k
print(df.sort_values("Isim"))#ismegore






