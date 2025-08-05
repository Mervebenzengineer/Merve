import tkinter as tk
import matplotlib.pyplot as plt

pencere=tk.Tk()
pencere.title("Ogrenci Not Grafigi")
pencere.geometry("300x200")

isimler=[]
notlar=[]

isim_label=tk.Label(pencere,text="Isim:")
isim_label.pack()

isim_entry=tk.Entry(pencere)
isim_entry.pack()

not_label=tk.Label(pencere,text="Not:")
not_label.pack()

not_entry=tk.Entry(pencere)
not_entry.pack()

ogrenci_listesi=[]
def kaydet():
    isim=isim_entry.get()
    notu=not_entry.get()

    if isim and notu:
        ogrenci_listesi.append((isim,notu))
        sonuc_label.config(text=f"{isim} adli ogrenci eklendi.")
        isim_entry.delete(0,tk.END)
        not_entry.delete(0,tk.END)
    
    else:
        sonuc_label.config(text="Lutfen tum alanlari doldurun!")
kaydet_buton=tk.Button(pencere,text="Kaydet",command=kaydet)
kaydet_buton.pack()

def listele():
    sonuc_label.config(text="Ogrenciler:")
    for ogrenci in ogrenci_listesi:
        print(f"isim:{ogrenci[0]},Not:{ogrenci[1]}")

listele_buton=tk.Button(pencere,text="Listele",command=listele).pack()

sonuc_label=tk.Label(pencere,text="")
sonuc_label.pack()

def grafik_ciz():
    if ogrenci_listesi:
        isimler=[ogr[0]for ogr in ogrenci_listesi]
        notlar=[int(ogr[1]) for ogr in ogrenci_listesi]

        plt.figure(figsize=(6,4))
        plt.bar(isimler,notlar,color="skyblue")
        plt.title("Ogrenci Not Grafigi")
        plt.xlabel ("Ogrenci Isimleri")
        plt.ylabel("Notlar")
        plt.ylim(0,100)
        plt.tight_layout()
        plt.show()
    else:
        sonuc_label.config(text="Liste bos,once ogrenci ekleyin.")

grafik_buton=tk.Button(pencere,text="Grafik Ciz",command=grafik_ciz)
grafik_buton.pack()

pencere.mainloop() #en son satir bu olmali 


   




 