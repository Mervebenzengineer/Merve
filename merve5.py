def not_ekle():
    not_metni = input("Kaydetmek istediginiz notu yazin:")
    with open("notlar.txt","a") as dosya:
        dosya.write( not_metni + "\n")
    print("Not basariyla kaydedildi!\n")
def notlari_oku():
    try:
        with open("notlar.txt","r") as dosya:
            icerik=dosya.read()
        print("Kayitli notlar:\n")
        print(icerik)
    except FileNotFoundError:
        print("Not kaydedilmemis.\n")
not_ekle()
notlari_oku()

def menu():
    while True:
        print("---NOT DEFTERI---")        
        print("1.Not ekle")
        print("2.Notlari Goruntule")
        print("3.Cik")

        secim=input("Seciminiz(1-2-3):")
        if secim=="1":
            not_ekle()
        elif secim=="2":
            notlari_oku()
        elif secim=="3":
            print("Programdan cikiliyor...")
            break
    else:
         print("Gecersiz secim.Lutfen 1,2 ya da 3 girin")
