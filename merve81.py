import time

print("Bekleniyor...")
time.sleep(3)
print("3 saniye sonra bu mesaj cikti!")

start= time.time()

for i in range(1000000):
    pass
end= time.time()

print("Islem suresi:",end-start,"saniye")

zaman=time.localtime()
print("Yil:",zaman.tm_year)
print("Saat:",time.strftime("%H:%M:%S",zaman))


