from bs4 import BeautifulSoup
import requests,sys,csv,json
import urllib



url = "http://ufm.edu/Portal"
r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")


def pages():
    direccion = soup.find(id='footer').find('a').text
    numero_email = soup.find(id = 'footer').find_all('a')
    #nav menu

    nav_menu= soup.find("table", {"id": "menu-table"})


    #links
    link = ""
    links= soup.find_all('a', href= True)
    for x in links:
        #if x.text.isalpha()== True:
        link += f"=> {x.text.strip()}\n"


    ufmail = soup.find(id = 'ufmail_')
    ufmailhref = ufmail.get('href')
    boton_miu = soup.find(id="miu_")
    botonMiuHref = boton_miu.get('href')

    #Imagenes
    img = ""
    imagenes = soup.find_all('img')
    for i in imagenes:
        img += f"=> {i['src']}\n"

    contadorA = soup.findAll('a')


    #1.1 extra points :) !
    #with open('csv.csv', 'w') as csvfile:
     #   escritor = csv.writer(csvfile, delimeter=',')
#
 #       for a in soup.findAll('a'):
  #          texto = a.string
   #         href = a['href']
    #        escritor.writerow(f'{texto}', f'{href}')
    #csvfile.close()

    print("BORIS RENDÓN")
    print("1. Portal")
    print("Titulo: \n", soup.title.string)
    print("Direccion: \n",direccion)
    print("E-mail y Correo: \n",numero_email[1].text, numero_email[2].text)
    print("Navmenu:\n", nav_menu.text.strip())
    print("Links: ", link.strip())
    print("href de UFMail: \n", ufmailhref)
    print("Boton Miu:\n ",botonMiuHref)
    print("href de todos los <img>:\n ", img)
    print("Contador <a>: \n", str(len(contadorA)))