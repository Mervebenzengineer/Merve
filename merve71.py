#Tkinter'a giris -Temel arayuz GUI uygulamasi

import tkinter as tk

pencere=tk.Tk()
pencere.title("Kullanci Bilgi Formu")
pencere.geometry("300x200")

tk.Label(pencere,text="isim:").pack()
isim_giris=tk.Entry(pencere)
isim_giris.pack()

tk.Label(pencere,text="Yas:").pack()
yas_giris=tk.Entry(pencere)
yas_giris.pack()

def bilgiyi_goster():
    isim=isim_giris.get()
    yas=yas_giris.get()
    tk.Label(pencere,text=f"Girilen Bilgi:{isim},{yas}").pack()

tk.Button(pencere, text="Gonder",command=bilgiyi_goster).pack()

pencere.mainloop()

