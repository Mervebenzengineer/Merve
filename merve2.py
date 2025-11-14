not1=int(input("1.sinav notunu gir:"))
not2=int(input("2.sinav notunu gir:"))
not3=int(input("3.sinav notunu gir:"))

ortalama=(not1+not2+not3)/3
print("Ortalma:",ortalama)
if ortalama>=60:
    print("Tebrikler,gectin")
else:
    print("Uzgunum,kaldin.")
