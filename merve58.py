ogrenciler = {
    "1001": {"ad": "Merve", "soyad": "Yılmaz", "notlar": [90, 85, 100]},
    "1002": {"ad": "Can", "soyad": "Demir", "notlar": [80, 75, 70]}
}

def ogrenci_ekle():
    numara = input("Öğrenci numarası: ")
    ad = input("Adı: ")
    soyad = input("Soyadı: ")
    notlar = list(map(int, input("Notları aralarına boşluk koyarak girin (örn: 90 85 100): ").split()))
    ogrenciler[numara] = {"ad": ad, "soyad": soyad, "notlar": notlar}

def ogrenci_listele():
    for no, bilgi in ogrenciler.items():
        print(f"{no} - {bilgi['ad']} {bilgi['soyad']}, Notlar: {bilgi['notlar']}")

def ogrenci_ara():
    no = input("Öğrenci numarası girin: ")
    if no in ogrenciler:
        print(f"{no} - {ogrenciler[no]['ad']} {ogrenciler[no]['soyad']}, Notlar: {ogrenciler[no]['notlar']}")
    else:
        print("Öğrenci bulunamadı.")

def not_guncelle():
    no = input("Öğrenci numarası: ")
    if no in ogrenciler:
        yeni_notlar = list(map(int, input("Yeni notları girin: ").split()))
        ogrenciler[no]["notlar"] = yeni_notlar
    else:
        print("Öğrenci bulunamadı.")

def ortalama_hesapla():
    for no, bilgi in ogrenciler.items():
        ort = sum(bilgi["notlar"]) / len(bilgi["notlar"])
        print(f"{no} - {bilgi['ad']} Ortalama: {ort:.2f}")

while True:
    print("\n1. Öğrenci Ekle")
    print("2. Öğrenci Listele")
    print("3. Öğrenci Ara")
    print("4. Not Güncelle")
    print("5. Ortalamaları Göster")
    print("6. Çıkış")
    secim = input("Seçiminiz: ")

    if secim == "1":
        ogrenci_ekle()
    elif secim == "2":
        ogrenci_listele()
    elif secim == "3":
        ogrenci_ara()
    elif secim == "4":
        not_guncelle()
    elif secim == "5":
        ortalama_hesapla()
    elif secim == "6":
        print("Programdan çıkılıyor...")
        break
    else:
        print("Geçerli seçim yapınız.")
