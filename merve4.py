not_metni=input("Kaydetmek istediginiz notu yazin ")
with open("notlar.txt","a")as dosya:
    dosya.write(not_metni+"\n")
    print("Not basariyla kaydedildi!")

with open("notlar.txt","r") as dosya:
    icerik = dosya.read()
print("Kayitli notlar:")
print(icerik)
input("Cikmak icin enter tusuna basin ")
exit()
