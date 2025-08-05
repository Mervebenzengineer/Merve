import tkinter as tk

pencere=tk.Tk()
pencere.title("Isim Gosterici")
pencere.geometry("300x200")

etiket=tk.Label(pencere,text="Isminizi girin:")
etiket.pack()

isim_giris=tk.Entry(pencere)
isim_giris.pack()

sonuc_etiket=tk.Label(pencere,text="")
sonuc_etiket.pack()

def metni_cek():
    isim=isim_giris.get()
    sonuc_etiket.config(text=f"Merhaba,{isim}!")

buton=tk.Button(pencere,text="Goster",command=lambda:metni_cek())
buton.pack()

pencere.mainloop()
