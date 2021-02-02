import requests
from bs4 import BeautifulSoup
import os
import time

url = "https://www.wallpaperflare.com/search?wallpaper=Islamic&page=1"

headers = {
    'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
    }

response = requests.request("GET", url, headers=headers)

data = BeautifulSoup(response.text, 'html.parser')

images = data.find_all('img', src=True)

image_src = [x['src'] for x in images]

image_src = [x for x in image_src if x.endswith('.jpg')]

for image in image_src:
    print(image)
