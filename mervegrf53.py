#dict yapisi
ogrenci={
    "isim":"Merve",
    "yas":23,
    "bolum":"Bilgisayar",
    "not":"99"
}
ogrenci["yas"]="24"
ogrenci["okul"]="ISTE"
del ogrenci["not"]
print(ogrenci.items())