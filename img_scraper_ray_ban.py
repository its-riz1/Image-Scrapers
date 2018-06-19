import urllib3
import requests
import urllib.request
from bs4 import BeautifulSoup

i=1
j=1
turn=0

def make_soup(url):
    source_code = requests.get(url)
    plain_text = source_code.text
    soupdata = BeautifulSoup(plain_text, "lxml")
    return soupdata

pages = 0
max_pages = 1 
while pages < max_pages :
    #give the required url and call the function
    url_make = "https://india.ray-ban.com/sunglasses-store.html?pg=" + str(pages)
    soup = make_soup(url_make)

    for div in soup.findAll('img', { 'class' : 'test' }):
        location_link = str((div.get('data-original')))
        string = location_link
        extention = str(string[len(string)-3:len(string)])
        imagefile = open("ray ban glasses/"+str(j)+"."+extention,"wb")
        # imagefile = open("ray ban glasses/"+str(j)+".png","wb")
        imagefile.write(urllib.request.urlopen(string).read())
        imagefile.close()
        i=i+1
        j=j+1
