kitap_sozlugu={
    "kitap_adi1":"Sefiller",
    "yazar1":"VHugo",
    "yil1":"2025",
    "kitap_adi2":"Kole",
    "yazar2":"Merve",
    "yil2":"2026"
}
# Listeyi gösteren fonksiyon
def listeyi_goster():
    for kitap, bilgi in kitap_sozlugu.items():
        print(f"{kitap} - yazar: {bilgi['yazar']} - yıl: {bilgi['yil']}")

while True:
    print("\n--- Kitap Takip Sistemi ---")
    print("1. Kitap ekleyin")
    print("2. Kitap silin")
    print("3. Listeyi gösterin")
    print("4. Kitap ara")
    print("5. Çıkış")
    secim = input("Seçiminizi yapın: ")

    if secim == "1":
        kitap_adi = input("Kitap adı girin: ")
        yazar = input("Yazar: ")
        yil = input("Yıl: ")
        kitap_sozlugu[kitap_adi] = {"yazar": yazar, "yil": yil}
        print(f"{kitap_adi} başarıyla eklendi.")

    elif secim == "2":
        silinecek = input("Silinecek kitap adı: ")
        if silinecek in kitap_sozlugu:
            del kitap_sozlugu[silinecek]
            print("Kitap silindi.")
        else:
            print("Kitap bulunamadı.")

    elif secim == "3":
        listeyi_goster()

    elif secim == "4":
        aranan = input("Aranan kitap adı: ")
        if aranan in kitap_sozlugu:
            bilgi = kitap_sozlugu[aranan]
            print(f"{aranan} - yazar: {bilgi['yazar']} - yıl: {bilgi['yil']}")
        else:
            print("Kitap bulunamadı.")

    elif secim == "5":
        print("Çıkılıyor...")
        break

    else:
        print("Geçerli bir seçim yapın.")
