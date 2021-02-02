
import urllib.request 
from bs4 import BeautifulSoup

wiki = "https://generator.email/blog/gmail-generator"

page = urllib.request.urlopen(wiki) 

soup = BeautifulSoup(page,features='html.parser')


all_links = soup.find_all('a')




if len(all_links) > 30 :
  
  last_5 = all_links[len(all_links)-30:]
  for url in last_5 :
    print(url.get('href'))

emails = []
for url in all_links :
    if(str(url.get('href')).find('@') > 0):
        emails.append(url.get('href'))


print(len(emails))

print('\n\nHasil Email: ')
for email in emails[:30]:
    print(email)
