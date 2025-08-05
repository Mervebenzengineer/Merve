import tkinter as tk
from tkinter import messagebox
import sqlite3 

def veri_kaydet():
    Isim=isim_entry.get()
    Numara=numara_entry.get()

    if not Isim or not Numara or not yas_entry.get():
        messagebox.showwarning("Uyari","Lutfen tum alanlari doldurun!")
        return


    yas=int(yas_entry.get())

 
    conn=sqlite3.connect("ogrenciler.db")
    cursor=conn.cursor()

    cursor.execute(
        "INSERT INTO ogrenciler(isim,numara,yas)VALUES(?,?,?)",(Isim,Numara,yas)
    )
    conn.commit()
    conn.close()

    messagebox.showinfo("Basarili","Ogrenci basariyla eklendi!")


    isim_entry.delete(0,tk.END)
    numara_entry.delete(0,tk.END)
    yas_entry.delete(0,tk.END)

def verileri_goster():
    
    conn=sqlite3.connect("ogrenciler.db")
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM ogrenciler")
    kayitlar=cursor.fetchall()
    conn.close()

    liste_pencere=tk.Toplevel()
    liste_pencere.title("Kayitli Ogrenciler")

    for i,kayit in enumerate(kayitlar):
        kayit_str=f"{i+1}.Isim:{kayit[0]}, Numara:{kayit[1]},Yas:{kayit[2]}"
        etiket=tk.Label(liste_pencere,text=kayit_str)
        etiket.pack()
 
def veri_sil():
    numara=sil_entry.get()
    if not numara:
        messagebox.showwarning("Uyari","Lutfen silinecek numarayi girin!")
        return
    conn=sqlite3.connect("ogrenciler.db")
    cursor=conn.cursor()

    cursor.execute("DELETE FROM ogrenciler WHERE numara=?",(numara,))
    conn.commit()
    conn.close()
    
    messagebox.showinfo("Basarili",f"{numara} numarali ogrenci silindi.")

    sil_entry.delete(0,tk.END)


pencere=tk.Tk()
pencere.title("Ogrenci Kayit Formu")
pencere.geometry("500x500")

isim_label=tk.Label(pencere,text="Isim:")
isim_label.pack()
isim_entry=tk.Entry(pencere)
isim_entry.pack()

numara_label=tk.Label(pencere,text="Numara:")
numara_label.pack()
numara_entry=tk.Entry(pencere)
numara_entry.pack()

yas_label=tk.Label(pencere,text="Yas:")
yas_label.pack()
yas_entry=tk.Entry(pencere)
yas_entry.pack()

sil_label=tk.Label(pencere,text="Silinecek Numara:")
sil_label.pack()
sil_entry=tk.Entry(pencere)
sil_entry.pack()

kaydet_buton=tk.Button(pencere,text="Kaydet",command=veri_kaydet)
kaydet_buton.pack()

goster_buton=tk.Button(pencere, text="Kayitlari Goster", command=verileri_goster)
goster_buton.pack()

sil_buton=tk.Button(pencere,text="Sil",command=veri_sil)
sil_buton.pack()




pencere.mainloop()


