from bs4 import BeautifulSoup
import requests

parser = 'html.parser'
resp = requests.get("https://google.com")
soup = BeautifulSoup(resp.content, parser)

for link in soup.find_all('a', href=True):
    print(link['href'])
