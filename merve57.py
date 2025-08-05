#Film Arşivi — Her film için adı, yönetmeni, yılı tutulsun. Ekle, sil, listele, ara, çık gibi seçenekler eklensin.

#Film Arşivi — Her film için adı, yönetmeni, yılı tutulsun. Ekle, sil, listele, ara, çık gibi seçenekler eklensin.

film={
    "ad":"scarface",
    "yonetmeni":"alpacino",
    "yil":"2000"
}
while True:
    print("1.Film ekle")
    print("2.Listele")
    print("3.Film ara")
    print("4.Listeden cik")
    secim=input("Secim yapiniz")
    if secim=="1":
        isim=input("Eklenecek film adi yazin")
        yonetmen=input("Yonetmen adi girin")
        yil=input("yili girin")
        film[isim]={"isim":ad, "yonetmen":yonetmen, "yil":yil}
        print(f"{isim}basariyla eklendi.")
    if secim=="2":
        for ad,bilgi in film.items():
            print(f"{ad}-yonetmen:{bilgi['yonetmen']},yil:{bilgi['yil']}")

    if secim=="3":
        aranan=input("Aramak istediginiz film adi:")
        if aranan in film:
            bilgi=film[aranan]
            print(f"{aranan}-yonetmen:{bilgi['yonetmen']},yil:{bilgi['yil']}")
        else:
             print("Film bulunamadi")
    elif secim=="4":
        break
    else:
         print("Gecerli secim yapiniz")


                    







