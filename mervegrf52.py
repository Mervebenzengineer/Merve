#NOT HESAPLAMA
#TUM KONU ICERIR
#Yapılacaklar:
 #Kullanıcıdan 5 dersin adını ve notlarını al
#Ortalama, max, min hesapla
#Tüm notları bar chart ile göster
#Sonuçları rapor.txt dosyasına yaz
#Grafik dosyasını notlar.png olarak kaydet

import matplotlib.pyplot as plt

def not_hesaplama_programi():
    dersler=[]
    notlar=[]
    for i in range (5):
        ders=input(f"{i+1}.dersin adini girin:")
        dersler.append(ders)

        while True:
            try:
                puan=float(input (f"{ders} notunu girin"))
                if 0<=puan<=100:
                    notlar.append(puan)
                    break
                else:
                    print("Not 0 ile 100 arasinda girin")
            except ValueError:
                print("Gecerli bir sayi girin")
    print("Girilen notlar",notlar)

    ortalama=sum(notlar)/len(notlar)
    en_yuksek=max(notlar)
    en_dusuk=min(notlar)

    plt.bar(dersler,notlar,color="skyblue")
    plt.title("Ders Notlari")
    plt.xlabel("Dersler")
    plt.ylabel("Notlar")
    plt.ylim(0,100)
    plt.tight_layout()

    plt.savefig("notlar.pdf")
    plt.show()

    with open("rapor.txt","w") as dosya:
        for i in range(5):
            dosya.write(f"{dersler[i]}:{notlar[i]}\n")
        dosya.write(f"\nOrtalama:{ortalama:.2f}\n")
        dosya.write(f"En yuksek Not:{en_yuksek}\n")
        dosya.write(f"En Dusuk Not:{en_dusuk}\n")
    print("\n Islem tamamlandi")
not_hesaplama_programi()




   

