#JSON DEVAMI

import json

students=[
    {"isim":"Merve","number":675,
     "dersler":[
     {"ad":"Matematik","not":99},
     {"ad":"Fizik","not":88}
     ]
    },
    
]

with open("students.json","w") as dosya:
    json.dump(students,dosya)

with open("students.json","r") as dosya:
    deger=json.load(dosya)


new_student=[
    {"isim":"Can",
    "number":980,
    "dersler":[{"ad":"Matematik","not":90},
    {"ad":"Fizik","not":76}
    ]
   },
]

deger.append(new_student[0])
with open("students.json","w") as dosya:
    json.dump(deger,dosya)



for student in deger:
    print("isim:",student["isim"])
    print("number:",student["number"])
    for ders in student["dersler"]:
        print(f"Ders:{ders['ad']},Not:{ders['not']}")
   
    print("-"*20)




