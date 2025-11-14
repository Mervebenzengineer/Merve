metin = input("Uzun bir cümle giriniz: ")

# metnin tamamı alfanumerik mi kontrolü
print("Metin alfanumerik mi:", metin.isalnum())

# sadece harf ve sayıları al, küçük harfe çevir
temiz = "".join(c.lower() for c in metin if c.isalnum())
print("Temiz metin:", temiz)

# tersine çevir
ters = temiz[::-1]
print("Ters:", ters)
