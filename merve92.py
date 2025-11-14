import os

os.getcwd()          # Geçerli çalışma dizinini verir
os.listdir()         # Belirtilen dizindeki dosyaları listeler
os.mkdir("yeni")     # "yeni" adında klasör oluşturur
os.remove("dosya.txt")   # dosya.txt dosyasını siler
os.rmdir("yeni")     # "yeni" klasörünü siler
os.rename("a.txt", "b.txt")  # a.txt → b.txt olarak yeniden adlandırır

