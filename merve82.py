import time

suan=time.localtime()
formatli_saat=time.strftime("%d.%m.%Y-%H:%M:%S",suan)

print("Su anki zaman:",formatli_saat)

print("Program baslatiliyor...")
time.sleep(2)
print("Hos Geldiniz!")
print("Tarih ve saat:",time.strftime("%d.%m.%Y-%H:%M:%S",time.localtime()))
