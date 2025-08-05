import tkinter as tk
import sqlite3
from tkinter import messagebox

def veri_kaydet():
    isim=isim_entry.get()
    numara=numara_entry.get()
    notu=not_entry.get()
    yas=yas_entry.get()

    if not isim or not numara or not notu or not yas:
        messagebox.showwarning("Uyari","Lutfen tum alanlari doldurun!")
        return
    try:
        notu=int(notu)
        yas=int(yas)
    except  ValueError:
        messagebox.showerror("Hata","Not ve Yas sayi olmalidir!")
        return


    conn=sqlite3.connect("ogrenciler.db")
    cursor=conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ogrenciler(
    isim TEXT,
    numara TEXT,
    notu INTEGER,
    yas INTEGER
    )
    """)

    cursor.execute(
        "INSERT INTO ogrenciler(isim,numara,notu,yas) VALUES (?,?,?,?)",(isim,numara,notu,yas)
    )

    conn.commit()
    conn.close()

    messagebox.showinfo("Basarili","Ogrenci basariyla eklendi")
   
    isim_entry.delete(0,tk.END)
    numara_entry.delete(0,tk.END)
    not_entry.delete(0,tk.END)
    yas_entry.delete(0,tk.END)

def veri_guncelle():
    numara=numara_entry.get()
    yeninot=yeninot_entry.get()
    yeniyas=yeniyas_entry.get()

    if not numara or not yeninot or not yeniyas:
        messagebox.showwarning("Uyari","Lutfen tum alanlari doldurun.")
        return 
    try:
        yeninot=int(yeninot)
        yeniyas=int(yeniyas)
    
    except ValueError:
        messagebox.showwarning("Uyari","Not ve yas sayi olmali!")


    conn=sqlite3.connect("ogrenciler.db")
    cursor=conn.cursor()

    cursor.execute("UPDATE ogrenciler SET notu=?,yas=? WHERE numara=?",(yeninot,yeniyas,numara)) 

    conn.commit()
    conn.close()

    if cursor.rowcount==0:
        messagebox.showinfo("Sonuc",f"{numara} numarali ogrenci bulunamadi.")
    else:
        messagebox.showinfo("Basarili",f"{numara} numarali ogrenci guncellendi.")

def veri_ara():
    deger=numara_entry.get()

    if not deger:
        messagebox.showwarning("Uyari","Lutfen numarayi girin!")
        return 

    conn=sqlite3.connect("ogrenciler.db")
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM ogrenciler where numara=?",(deger,) )

    veriler=cursor.fetchone()

    conn.close()
    
    if veriler:
        sonuc_pencere=tk.Toplevel()
        sonuc_pencere.title("Arama Sonucu")

        sonuc_yazi=f"Isim:{veriler[0]}\n Numara:{veriler[1]}\nNot:{veriler[2]}\n Yas:{veriler[3]}"
        sonuc_label=tk.Label(sonuc_pencere,text=sonuc_yazi)
        sonuc_label.pack()
    else:
        messagebox.showinfo("Sonuc",f"{deger} numarali ogrenci bulunamadi.")


pencere=tk.Tk()
pencere.title("Ogrenci Kayit Sistemi")
pencere.geometry("500x500")

etiketler=["Isim","Numara","Notu","Yas"]
entryler=[]
for etiket in etiketler:
    tk.Label(pencere,text=etiket).pack()
    entry=tk.Entry(pencere)
    entry.pack()
    entryler.append(entry)
isim_entry,numara_entry,not_entry,yas_entry=entryler

tk.Button(pencere,text="Kaydet",comman=veri_kaydet).pack()

tk.Button(pencere,text="Guncelle",command=veri_guncelle).pack()

tk.Button(pencere, text="Ara", command=veri_ara).pack()

pencere.mainloop()



isim_label=tk.Label(pencere, text="Isim")
isim_label.pack()

isim_entry=tk.Entry(pencere)
isim_entry.pack()

numara_label=tk.Label(pencere,text="Numara")
numara_label.pack()

numara_entry=tk.Entry(pencere)
numara_entry.pack()

not_label=tk.Label(pencere,text="Notu")
not_label.pack()

not_entry=tk.Entry(pencere)
not_entry.pack()

yas_label=tk.Label(pencere, text="Yas")
yas_label.pack()

yas_entry=tk.Entry(pencere)
yas_entry.pack()

kaydet_buton=tk.Button(pencere,text="Kaydet" ,command=veri_kaydet)

kaydet_buton.pack()

guncelle_buton=tk.Button(pencere,text="Guncelle", command=veri_guncelle)
guncelle_buton.pack()

ara_buton=tk.Button(pencere,text="Ara",command=veri_ara)
ara_buton.pack()

pencere.mainloop()


