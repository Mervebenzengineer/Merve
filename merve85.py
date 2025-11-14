import json
#json verisini dosyaya yazmak(json.dump())

veri={
    "name":"Merve",
    "bolum":"Bilg Muh",
    "age":23
}

with open("veri.json","w") as dosya:
    json.dump(veri,dosya)

#json dosyasindan veri okumak(json.load())

with open("veri.json","r") as dosya:
    veri=json.load(dosya)
print(veri["name"])