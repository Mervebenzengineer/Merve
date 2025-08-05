#df yapisinin normal ve tranpoz halini yazdirma 

import pandas as pd

veri={
    "Ogrenci1":{"isim":"Merve","Not":90,"yas":23},
    "Ogrenci2":{"isim":"Veda","Not":89,"yas":45},
    "Ogrenci3":{"isim":"can","Not":75,"yas"
    :56}

}
df=pd.DataFrame(veri)
print(df)

df_yeni=pd.DataFrame(veri).T
print(df_yeni)