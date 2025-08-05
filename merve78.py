#SIFRE SISTEMI

import tkinter as tk
from tkinter import messagebox

dogru_kullanici="merve"
dogru_sifre="8802"

def kontrol_et():
    kullanici_adi=dogru_kullanici_entry.get()
    girilen_sifre=dogru_sifre_entry.get()

    if kullanici_adi== dogru_kullanici and girilen_sifre==dogru_sifre:
     messagebox.showinfo("Basarili","Giris yapildi!")
    else:
        messagebox.showerror("Hata","Kullanici adi veya sifre yanlis!")
        
        dogru_kullanici_entry.delete(0,tk.END)
        dogru_sifre_entry.delete(0,tk.END)

pencere=tk.Tk()
pencere.title("Sifre Sistemi")
pencere.geometry("500x300")


dogru_kullanici_label=tk.Label(pencere,text="Kullanici Adi:")

dogru_kullanici_label.pack()

dogru_kullanici_entry=tk.Entry(pencere)

dogru_kullanici_entry.pack()

dogru_sifre_label=tk.Label(pencere,text="Sifre:")

dogru_sifre_label.pack()

dogru_sifre_entry=tk.Entry(pencere,show="*")

dogru_sifre_entry.pack()

kontrol_buton=tk.Button(pencere,text="Kontrol",command=kontrol_et)

kontrol_buton.pack()

pencere.mainloop()


