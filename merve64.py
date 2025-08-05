#DataFrame olusturma
import pandas as pd 
veri={
    "Isim":["Merve","can","a"],
    "Not":[90,86,78],
    "yas":[23,34,18]
}
df=pd.DataFrame(veri)
print(df)