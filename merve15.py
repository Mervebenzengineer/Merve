def tersine_cevir(metin):
     return metin[::-1]
 
    
def kalin_harf_say(metin):
    kalin="aeiouAEIUO"
    sayac=0
    for harf in metin:
        if harf in kalin:
            sayac+=1
    return sayac
   
def palindrom_mu(metin):
    temiz="".join(c.lower()for c in metin if c.isalnum())
    return temiz==temiz[::-1]

metin=input("Metin girin")
print("Tersine:",tersine_cevir(metin))
print("Kalin sesli harf sayisi:",kalin_harf_say(metin))
print("Palindron:","Evet" if palindrom_mu(metin)else "Hayir")
