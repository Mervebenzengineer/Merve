import xml.etree.ElementTree as ET

book=ET.Element("book")

name=ET.SubElement(book,"name")
name.text="Sefiller"

writer=ET.SubElement(book,"writer")
writer.text="Victor Hugo"

page=ET.SubElement(book,"page")
page.text="500"


tree=ET.ElementTree(book)
tree.write("dosya.xml")

tree=ET.parse("dosya.xml")

root=tree.getroot()

for eleman in root:
    print(eleman.tag,":",eleman.text)



