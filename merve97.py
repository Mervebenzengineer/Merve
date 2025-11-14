import shutil
import os

os.makedirs("yedekler",exist_ok=True)
os.makedirs("gecmis",exist_ok=True)


shutil.copy("rapor.txt","yedekler/rapor.txt")

shutil.copy2("rapor.txt","yedekler.txt")

shutil.move("rapor.txt","gecmis/rapor.txt")

shutil.rmtree("yedekler")

