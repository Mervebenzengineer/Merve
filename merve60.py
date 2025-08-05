ogrenciler={
    "1001":{"isim":"Merve","not":90},
    "1002":{"isim":"Sevda","not":95},
    "1003":{"isim":"Can","not":99}
}
while True:
   print("1.Ogrenci  notu listele")
   print("2.Cikiliyor...\n")
   secim=input("Seciminizi yapin")

   if secim=="1":
      for no,bilgi in ogrenciler.items():
        print(f"No:{no}|isim: {bilgi['isim']}| Not:{bilgi['not']}")
   if secim=="2":
      print("Cikiliyor")
      break
   else:
      print("Gecersiz secim.Yeniden giris yapin")

   
      
