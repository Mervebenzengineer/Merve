import shutil
import os

shutil.copy("deneme.txt","yedek/deneme.txt")

shutil.move("yedek/deneme.txt","arsiv/deneme.txt")


shutil.rmtree("yedek")
