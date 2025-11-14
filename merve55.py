ogrenciler = {
    "2425": {"isim": "Veli", "not": "99"},
    "3536": {"isim": "Can", "not": "56"}
}

while True:
    print("\n--- MENU ---")
    print("1. Ogrenci ekle")
    print("2. Ogrenci sil")
    print("3. Not guncelle")
    print("4. Ogrencileri listele")
    print("5. Cikis")

    secim = input("Seciminizi yapin: ")

    if secim == "1":
        numara = input("Ogrenci numara: ")
        isim = input("Ad: ")
        notu = input("Notu: ")
        ogrenciler[numara] = {"isim": isim, "not": notu}
        print("Ogrenci eklendi.")

    elif secim == "2":
        numara = input("Silinecek ogrenci numara: ")
        if numara in ogrenciler:
            del ogrenciler[numara]
            print("Ogrenci silindi.")
        else:
            print("Bu numara bulunamadi!")

    elif secim == "3":
        numara = input("Guncellenecek ogrenci numara: ")
        if numara in ogrenciler:
            yeni_not = input("Yeni Not: ")
            ogrenciler[numara]["not"] = yeni_not
            print("Not guncellendi.")
        else:
            print("Bu numara bulunamadi!")

    elif secim == "4":
        for numara, bilgiler in ogrenciler.items():
            print(f"Numara: {numara}, Isim: {bilgiler['isim']}, Not: {bilgiler['not']}")

    elif secim == "5":
        print("Programdan cikiliyor...")
        break

    else:
        print("Hatali secim yaptiniz!")
