import sqlite3

conn=sqlite3.connect("ogrenciler.db")#.db dosyasini olusturur.
cursor=conn.cursor()#SQL komutlarini calistirmak icin kanal 

cursor.execute("""
CREATE TABLE IF NOT EXISTS ogrenciler(
    isim TEXT,
    numara TEXT,
    notu INTEGER,
    yas INTEGER
)
""")

#cursor.execute(
 #   "INSERT INTO ogrenciler(isim,numara,notu,yas)VALUES (?,?,?,?)",
  #  ("Merve","1001",95,20))


isim=input("Isim:")
numara=input("Numara:")
notu=int(input("Notu:"))
yas=int(input("Yas:"))

cursor.execute("INSERT INTO ogrenciler(isim,numara,notu,yas) VALUES (?,?,?,?)",(isim,numara,notu,yas)) #girilen bilgileri veritabanına ekler.

    

cursor.execute("SELECT * FROM ogrenciler") #sorguyu veritabanina gonderir

veriler=cursor.fetchall()

for v in veriler:
    print(v)


conn.commit()#yapilan degisiklik kaydedilir

conn.close()#baglantiyi kapat
#text:metin integer:tam sayi 

