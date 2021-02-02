
'''imports'''
from geolite2 import geolite2
import requests


def my_ip_location(my_ip):
    reader = geolite2.reader()
    location = reader.get(my_ip)

    #geolite database dict values and fine tunning
    b=(location['continent']['names']['en'])
    c=(location['country']['names']['en'])
    d=(location['location'])
    f=(location['registered_country']['names']['en'])
    g=(location['subdivisions'][0]['names']['en'])

    print('''continent: %s\ncountry: %s\nlocation: %s/\nregistered_country: %s\nsubdivisions: %s\n'''
     % (b,c,d,f,g))


my_ip = input("Masukkan IP: ")

my_ip_location(my_ip)
