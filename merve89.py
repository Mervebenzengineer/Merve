#XML

import xml.etree.ElementTree as ET

# 1. XML oluştur
ogrenci = ET.Element("ogrenci")  # kök

isim = ET.SubElement(ogrenci, "isim")
isim.text = "Merve"

numara = ET.SubElement(ogrenci, "numara")
numara.text = "674"

bolum = ET.SubElement(ogrenci, "bolum")
bolum.text = "Bilgisayar"

# 2. XML dosyasına yaz
tree = ET.ElementTree(ogrenci)
tree.write("ogrenci.xml")

# 3. Dosyadan oku
tree = ET.parse("ogrenci.xml")
root = tree.getroot()

# 4. Etiketleri yazdır
for eleman in root:
    print(eleman.tag, ":", eleman.text)

"""
ET.Element("etiket")	Yeni bir XML etiketi oluşturur
ET.SubElement(ebeveyn, "alt_etiket")	Mevcut etiketin altına başka bir etiket ekler
.text = "yazı"	Etiketin içine metin yazar
ET.ElementTree(root)	XML ağacı oluşturur
.write("dosya.xml")	XML'i dosyaya kaydeder
.parse("dosya.xml")	Dosyadaki XML’i okur
.getroot()	Kök etiketi döner
.tag	Etiketin adını verir
.text	Etiketin içindeki veriyi verir
"""