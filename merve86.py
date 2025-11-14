import json
#json dosyasindan veri okumak(json.load())

veri={
    "name":"Merve",
    "job":"Bilg Muh",
    "age":23
}

with open("veri.json","w") as dosya:
    json.dump(veri,dosya)

with open("veri.json","r") as dosya:
    okunan_veri=json.load(dosya)
    
print(okunan_veri)

#Okunan kod dosyadan okunan sonucu degil,ilk halini yazdirir.
#veri:python;da en basta tanimlanan sozluk
#okunan_veri:Dosyadan JSON olarak okunan sonucu degil,ilk halini yazdirir.