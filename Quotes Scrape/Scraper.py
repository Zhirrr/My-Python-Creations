from bs4 import BeautifulSoup
import requests

url = requests.get("https://jagokata.com/kata-bijak/acak.html")

soup = BeautifulSoup(url.content, 'html.parser')

for anjay in soup.find_all('q', class_='fbquote'):
  print(anjay.text)
