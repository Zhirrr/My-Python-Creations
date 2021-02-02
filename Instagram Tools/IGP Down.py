import requests, json
import sys

#Banner
print('''

-----------------------------------------------------------
                Instagram Profile Downloader
------------------------------------------------------------
############################################################
     [+] Author : Zhirrr
     [+] Follow My IG : zhirr_ajalah
     [+] Follow My Github : Zhirrr
############################################################

''')
              

msg = input("Masukkan Username: ")
r = requests.get("https://xmadd4.herokuapp.com/api/stalk?username="+msg)
j = json.loads(r.text)
print ("URL Profil: "+j["Profile_pic"])

d= input("Download? (Y/n): ")
if d == "Y" or d == "y":
	r = requests.get(j["Profile_pic"]).content
	open('/storage/emulated/0/profile.png', 'wb').write(r)
	
	if d == "N" or d == "n":
		sys.exit()
