from bs4 import BeautifulSoup
import os
import time
import requests

url = input("Masukkan URL: ")

headers = {
    'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
    }

response = requests.request("GET", url, headers=headers)

data = BeautifulSoup(response.text, 'html.parser')

images = data.find_all('img', src=True)

image_src = [x['src'] for x in images]

image_src = [x for x in image_src if x.endswith('.jpg')]

image_count = 1
for image in image_src:
    with open('image_'+str(image_count)+'.jpg', 'wb') as f:
        res = requests.get(image)
        f.write(res.content)
    image_count = image_count+1
