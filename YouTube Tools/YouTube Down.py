import youtube_dl,os

#CopyRights 2020
#Code By Zhirrr Use Youtube_DL Libraries

yd = {}
path = '/storage/emulated/0'
os.chdir(path)
#Banner
print(''' 

------------------------------------------------------------
                   YouTube MP4 Downloader       
------------------------------------------------------------
                       Code By Zhirrr               
------------------------------------------------------------
#################################################
   [+] Author:  Zhirrr                      
   [+] Follow My IG:  zhirr_ajalah
   [+] Follow My GitHub:  Zhirrr
#################################################

''')
url = input("Masukkan URL YouTube: ")
with youtube_dl.YoutubeDL(yd) as y:
    print("MenDownload...."+url)
    y.download([url])
print("Video TerDownload")
