from __future__ import unicode_literals
import lxml.html as lh
import requests
import youtube_dl
import os 


#target = "/select/path"  # Zielordner innerhalb von home
website = "https://aufwachen-podcast.de/"

rq = requests.get(website)
content = rq.content
doc = lh.fromstring(content)

for elt in doc.xpath('//iframe'):
    url_data = elt.attrib.get('src')
    print url_data 
    #os.chdir(target) # zielverzeichnis festlegen
    ydl_opts = {}
    # try damit er nicht bei videos die im processing sind aussteigt
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url_data])
    except:
        pass 
