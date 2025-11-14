#   BINARY
def binary_search(arr,target):

    sol=0
    sag=len(arr)-1

    while sol<=sag:
        orta=(sol+sag)//2

        #hedef deger ortadaysa
        if arr[orta]==target:
            return orta
        
        #Eger hedef deger ortadaki degerden buyukse,sag taraf kontrol edilir

        elif arr[orta]>target:
            sag=orta-1

            #Eger hedef deger ortadaki degerden buyukse,sag taraf kontrol edilir

        else:
            sol=orta+1
            #hedef deger bulunmazsa
    return-1
        
liste=[2,4,6,8,10,12,14,16,18,20]
hedef=10

result=binary_search(liste,hedef)

if result!=-1:
    print(f"\nAranan eleman: {result} Indiste bulundu.")
else:
    print("Aranan eleman dizide bulunmadi.")





