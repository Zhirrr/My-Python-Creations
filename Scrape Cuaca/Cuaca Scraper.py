import requests
from bs4 import BeautifulSoup

page = requests.get('https://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?kab=Jakarta&Prov=DKI_Jakarta&AreaID=501195')
soup = BeautifulSoup(page.content, 'html.parser')

print("="*50,"\n")
print("          Web Scraping Data BMKG Terkini      \n")

datakota = soup.find('h4', attrs ={'class' : 'margin-bottom-30'}).get_text()
print("Provinsi  : ",datakota)

waktu = soup.find('h2', attrs ={'class' : 'kota'}).get_text()
print("Waktu     : ",waktu)

suhu = soup.find('h2', attrs ={'class' : 'heading-md'}).get_text()
print("Suhu      : ",suhu)

keterangan = soup.find('div', attrs = {'class' : 'service-block clearfix'})
keterangann = keterangan.find_next('p')
all=keterangann.text
print('Cuaca     : ',all,"\n")
print("="*50,"\n")
