from bs4 import BeautifulSoup
import requests,sys,csv,json
import urllib

url = "http://ufm.edu/Estudios"
r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")

#este template debería estar en todas las clases
print("BORIS RENDÓN")
print("2. Estudios")

#Navegar el href
hrefnav = soup.find('div',{'class': "menu-key"})

#top menu items , son 8

menutop = ""
menutop1 = soup.find_all("div", {'id': "topmenu"})
for i in menutop1:
    for li_item in i.find_all("li"):
        menutop += f"=> {li_item.text}\n"

# Display de estudios
estudiostop = ""
estudiostop1 = soup.find_all("div", {"class": "estudios"})
for x in estudiostop1:
    estudiostop += f"=> {x.text}\n"

# Leftbar items
leftbar = ""
leftbar1= soup.findAll("div", {"class":"leftbar"})
for left in leftbar1:
    for left_li in left.find_all("li"):
        leftbar += f"=> {left_li.text}\n"

#get and display all social media with its links 
socialmedia= ""
socialmedia1 = soup.find("div", {"class": "social pull-right"})
for social in socialmedia1.find_all('a'):
    socialmedia += "=>" + social['href']+ '\n'
#### 
print("Navegación: \n", hrefnav)
print("Items del menú: \n", menutop)
print("Items de estudios: \n", estudiostop)
print("Leftbar items: \n", leftbar)