from bs4 import BeautifulSoup
import requests,sys,csv,json
import urllib
import shutil

url =  "https://fce.ufm.edu/carrera/cs/"
r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")


# GET title


#GET and display href

###

# Download FCE logo

def compsci():
    print(" BORIS RENDÓN")
    print("3. Página Cs")
    logo1 = soup.find_all('a',href ="https://fce.ufm.edu")
    for i in logo1:
        fuente = i.find("img")['src']
    r1 = requests.get(fuente,stream=True)
    logo2= open('logo.jpg','wb')
    r1.raw.decode_content = True
    shutil.copyfileobj(r1.raw,logo2)
   

    #  GET following <meta>: "title", "description" ("og")
    metatitle = ""
    itemMeta = soup.find('meta', {'property':'og:title'})['content']
    for i in itemMeta:
        metatitle = f"{itemMeta}"

    metaDescription = ""
    itemDescription = soup.find('meta', {'property':'og:description'})['content']
    for description in itemDescription:
        metaDescription = f"{itemDescription}"

    #count all <a>
    ContadorA = soup.findAll('a')
    #Count all <div>
    ContadorDiv = soup.findAll('div')

    #Prints
    print("Titulo CS: \n" , soup.title.string)
    #print("Href: \n" , href)
    print("Logo FCE guardado como logo.jpg:\n")
    print("Meta title:\n" ,metatitle)
    print("Meta Description:\n" , metaDescription)
    print("Contador de <a>:\n ", str(len(ContadorA)))
    print("Contador de <div>:\n", str(len(ContadorDiv)))

