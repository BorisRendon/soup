from bs4 import BeautifulSoup
import requests,sys,csv,json
import urllib

url = "http://ufm.edu/Estudios"
r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")



#top menu items , son 8

menutop = ""
menutop1 = soup.find_all("div", {'id': "topmenu"})
for i in menutop1:
    for li_item in i.find_all("li"):
        menutop += f"=> {li_item.text}\n"


print(menutop)