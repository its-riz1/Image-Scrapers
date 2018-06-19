import urllib3
import requests
import urllib.request
import re
from bs4 import BeautifulSoup

i=1

def make_soup(url):
    source_code = requests.get(url)
    plain_text = source_code.text
    soupdata = BeautifulSoup(plain_text, "lxml")
    return soupdata

soup = make_soup("https://www.lenskart.com/sunglasses/")

for img in soup.find_all('img' , id = re.compile("productimgover_")):
    string = img.get('img-data-src')
    if string[0] == 'h' and str(string[111:112]+string[113:114]) != "le" and string[111:112] != 'M ' and string[113:114] != 'j' :
        extention = str(string[len(string)-3:len(string)])
        imagefile = open("lenskart glasses/"+str(i)+"."+extention,"wb")
        imagefile.write(urllib.request.urlopen(string).read())
        imagefile.close()
        i=i+1
    