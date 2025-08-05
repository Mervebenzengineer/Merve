#Tkinter ile Veritabaninda Arama

import tkinter as tk 
from tkinter import messagebox
import sqlite3

def veri_ara():
    deger=numara_entry.get()

    if not deger:
        messagebox.showwarning("Uyari","Lutfen numarayi girin")

    conn=sqlite3.connect("ogrenciler.db")
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM ogrenciler where numara=?",(deger,) )

    veriler=cursor.fetchone()

    conn.close()
    
    if veriler:
        sonuc_pencere=tk.Toplevel()
        sonuc_pencere.title("Arama Sonucu")

        sonuc_yazi=f"Isim:{veriler[0]}\n Numara:{veriler[1]}\n Not:{veriler[2]}\n Yas:{veriler[3]}"
        sonuc_label=tk.Label(sonuc_pencere,text=sonuc_yazi)
        sonuc_label.pack()
    else:
        messagebox.showinfo("Sonuc",f"{deger} numarali ogrenci bulunamadi.")

def veri_guncelle():
    deger=numara_entry.get()
    yeninot=yeninot_entry.get()
    yeniyas=yeniyas_entry.get()

    if not deger or not yeninot or not yeniyas:
        messagebox.showwarning("Uyari","Lutfen tum alanlari doldurun.")
        return 
    try:
        yeninot=int(yeninot)
        yeniyas=int(yeniyas)
    
    except ValueError:
        messagebox.showwarning("Uyari","Not ve yas sayi olmali!")


    conn=sqlite3.connect("ogrenciler.db")
    cursor=conn.cursor()
    cursor.execute("UPDATE ogrenciler SET notu=?,yas=? WHERE numara=?",(yeninot,yeniyas,deger)) 
    conn.commit()
    conn.close()

    if cursor.rowcount==0:
        messagebox.showinfo("Sonuc",f"{deger} numarali ogrenci bulunamadi.")
    else:
        messagebox.showinfo("Basarili",f"{deger} numarali ogrenci guncellendi.")
    
pencere=tk.Tk()
pencere.title("Tkinter ile Veritabaninda Arama")
pencere.geometry("500x500")

numara_label=tk.Label(pencere,text="numara:")
numara_label.pack()
numara_entry=tk.Entry(pencere)
numara_entry.pack()

yeninot_label=tk.Label(pencere,text="Yeni not:")
yeninot_label.pack()
yeninot_entry=tk.Entry(pencere)
yeninot_entry.pack()

yeniyas_label=tk.Label(pencere,text="Yeni yas:")
yeniyas_label.pack()
yeniyas_entry=tk.Entry(pencere)
yeniyas_entry.pack()

ara_buton=tk.Button(pencere,text="Ara",command=veri_ara)
ara_buton.pack()

guncelle_buton=tk.Button(pencere,text="Guncelle", command=veri_guncelle)
guncelle_buton.pack()


pencere.mainloop()
