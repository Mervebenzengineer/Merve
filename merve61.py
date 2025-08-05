kutuphane = {
    "K001": {"ad": "Sefiller", "yazar": "Victor Hugo", "yil": "1862"},
    "K002": {"ad": "Suç ve Ceza", "yazar": "Dostoyevski", "yil": "1866"},
}
while True:
    print("1.Kitap ekle")
    print("2.Kitap listele")
    print("3.Kitap sil")
    print("4.Kitap ara")
    print("5.Cikis")
    secim=input("Islem seciniz")

    if secim=="1":
        kitapkodu=input("Kitap kodu girin")
        kitapadi=input("Kitap adi girin")
        yazaradi=input("Yazar adi girin")
        yil=input("Yil girin")
        kutuphane[kitapkodu]={"ad":kitapadi,"yazar":yazaradi,"yil":yil}
        print(f"{kitapkodu} basariyla eklendi.")

    elif secim=="2":
        for kod,bilgi in kutuphane.items():
            print(f"{kod}-{bilgi['ad']}|yazar:{bilgi['yazar']}|yil:{bilgi['yil']}")

    elif secim=="3":
        silinecek=input("Silinecek kitap kodu girin")
        if silinecek in kutuphane:
            del kutuphane [silinecek]
            print("Kitap silindi")
        else:
            print("Kitap bulunamadi.")

    elif secim=="4":
        aranan=(input("Kitap    kodu girin"))
        if aranan in kutuphane:
                kitap=kutuphane[aranan]
                print(f"{aranan}:{kitap['ad']},Yazar:{kitap['yazar']},yil:{kitap['yil']}")
        else:
            print("Aranan kitap bulunamadi.")

    if secim=="5":
        print("Cikiliyor...")
        break
    else:
        print("Gecerli secim yapin")







