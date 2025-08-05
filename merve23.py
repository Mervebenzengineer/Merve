liste=[]
print("Sayi girin.Cikmak icin 'q' yazin")

while True:
      veri=input("Sayi:")
      if veri=="q":
            print("Dongu sonlandirildi.")
            break
      
      try:
            sayi=float(veri)
            liste.append(sayi)
      except ValueError:
            print("Gecerli sayi girin")
print("Sayi listesi",liste)




