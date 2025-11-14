import requests

isim=input ("Adinizi girin:")

if not isim.strip():
    print("Lutfen bos birakmayin!")
else:
    try:
        
        url=f"https://api.agify.io?name={isim}"

        response=requests.get(url)

        veri= response.json()

        print(f"{isim} ismine gore tahmini yas:{veri['age']}")
    except requests.exceptions.RequestException:
        print("API istegi basarisiz oldu!Internet baglantisini kontrol edin.")
    finally:
        print("Program sonlandi.")



#.json:Json veriyi Python dict'e cevirir.

#Doviz kuru cekmedede kullanilir.


