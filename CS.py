from bs4 import BeautifulSoup
import requests,sys,csv,json
import urllib

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
    Logo = soup.find("img", {"class": 'fl-photo-img wp-image-500 size-full' })
    strlogo = f"{Logo.get('src')}\n" 
    #imgUrl = soup.find(href="https://fce.ufm.edu").find('img')['src']

   # try:
    #    urllib.request.urlretrieve(imgUrl, os.path.basename('FCE_logo.png'))
    #except:
    #    print("No se encontró la imagen")

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
    print("Logo FCE:\n" , strlogo)
    print("Meta title:\n" ,metatitle)
    print("Meta Description:\n" , metaDescription)
    print("Contador de <a>:\n ", str(len(ContadorA)))
    print("Contador de <div>:\n", str(len(ContadorDiv)))

compsci()