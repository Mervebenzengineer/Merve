import json

#1.pythoni json'a donustur(json.dumps())


veri={
    "name":"Merve",
    "age":21,
    "student":True
}

json_veri=json.dumps(veri)
print(json_veri)

# json'i python sozlugune  donustur(json.loads())

json_metin='{"isim":"Merve","age":21,"student":true}'
veri=json.loads(json_metin)
print(veri["isim"])



