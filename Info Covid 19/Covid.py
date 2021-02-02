import json
from urllib import request

#Copyrights 2020
#Created By Zhirrr

url = "https://indonesia-covid-19.mathdro.id/api/provinsi"

response = request.urlopen(url)

data = json.loads(response.read())

for covid in data['data']:
    print("---------------------------")
    print("---------------------------")
    print(f"- {covid['provinsi']}:")
    
    print(f"  ðŸ¤•Positif: {covid['kasusPosi']}")
    
    print(f"  ðŸ¤—Sembuh: {covid['kasusSemb']}")
    
    print(f"  Meninggal: {covid['kasusMeni']}")
