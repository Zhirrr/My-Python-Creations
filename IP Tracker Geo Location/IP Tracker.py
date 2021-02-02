import pygeoip
import requests

#Coded By Zhirrr
#Copyrights 2020

#Banner
print('''
----------------------------------------------------------
                       IP Tracker
----------------------------------------------------------

''')

my_ip = input("Masukkan IP Yg Ingin Dilacak: ")

gip = pygeoip.GeoIP('GeoLiteCity.dat')

res = gip.record_by_addr(my_ip)

for key, val in res.items():
	print(f' {key} : {val} ')
