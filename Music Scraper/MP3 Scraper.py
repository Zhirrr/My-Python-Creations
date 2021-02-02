from bs4 import BeautifulSoup
import requests
 
url = 'https://telugump3audio.com/oh-baby-b.html'
 
 
res = requests.get(url).content
 
soup = BeautifulSoup(res,'html.parser')
 
data = soup.find_all('a')
 
 
for link in data:
    song_link = link['href']
    songs = link.text
 
    if '.mp3' in song_link:
        print(song_link)
