metin=input("Uzun bir cumle giriniz")

print("metin", metin.isalnum())

temiz="".join(c.lower()for c in metin if c.isalnum)
print("Temiz metin:",temiz)

ters="".join(temiz[::-1])
print(ters)

