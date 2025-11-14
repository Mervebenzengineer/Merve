import requests 

url= "https://api.github.com"

cevap=requests.get(url)
print(cevap.status_code)
