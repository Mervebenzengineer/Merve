import os

yol = "students.json"  

if os.path.exists(yol):
    print(f"{yol} bulundu.")
    
    if os.path.isfile(yol):
        print(f"{yol} bir dosyadır.")
    elif os.path.isdir(yol):
        print(f"{yol} bir klasördür.")
else:
    print(f"{yol} bulunamadı.")
