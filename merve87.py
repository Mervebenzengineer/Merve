import json

students=[
    {"isim":"Merve","number":675,
     "not":99},
    {"isim":"Sevda",
    "number":987,"not":100}
]

with open("students.json","w") as dosya:
    json.dump(students,dosya)

with open("students.json","r") as dosya:
    deger=json.load(dosya)

for student in deger:
    print("isim:",student["isim"])
    print("number:",student["number"])
    print("not:",student["not"])
    print("-"*20)




