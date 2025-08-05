ogrenciler={
    "isim":"veli",
    "numara":"2425",
    "not":"99",
    "isim":"can",
    "numara":"3536",
    "not":"56"
}
while True:
    print("1.Ogrenci ekle")
    print("2.Ogrenci sil")
    print("3.Not guncelle")
    print("4.Ogrencileri Listele")
    print("5.Cikis")

    secim=input("Seciminizi yapin:")
    if secim=="1":
        numara=input("Ogrenci nu:")
        isim=input("Ad:")
        notu=input("Notu:")
        ogrenciler[numara]={"ad":isim,"not":notu}
    elif secim=="2":
        del ogrenciler[numara]
    elif secim=="3":
        numara=input("Guncellenecek ogrenci numaara:")
        yeni_not=input("Yeni Not:")
        ogrenciler[numara]["not"]=yeni_not
    elif secim=="4":
        print(ogrenciler.items())
    else :
        break
del ogrenciler[numara]
del ogrenciler[notu]

