dogru=input("Gecerli anahtar girin")
anahtar={
        "proje":"MetanGazi",
        "tubitak":"semiha",
        "teknofest":"merve"
}
if dogru in anahtar:
    print("Dogru Giris Yaptiniz")
else:
    print("Hatali giris yaptiniz")

print(anahtar.items())
print(anahtar.keys())
print(anahtar.values())

  

