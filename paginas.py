from bs4 import BeautifulSoup
import requests,sys,csv,json

url = "http://ufm.edu/Portal"
r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")
output = soup.separator_parts 


direccion = soup.find(id='footer').find('a').text
numero_email = soup.find(id = 'footer').find_all('a')
nav_menu= soup.find(id = 'menu-table').find('td')
links= soup.find_all('a', href= True)
ufmail = soup.find(id = 'ufmail_').text + soup.find(id='ufmail_')['href']
boton_miu = soup.find(id='miu_').text + soup.find(id='miu_')['href']
imagenes = soup.find_all('img')
contadorA = soup.findAll('a')



print("BORIS RENDÓN")
print("1. Portal")
print("Titulo: ", soup.title.string)
print("Direccion: ",direccion)
print("E-mail y Correo: ",numero_email[1].text, numero_email[2].text)
print("Navmenu:", nav_menu)
print("Links: ", links)
print("href de UFMail: ", ufmail)
print("Boton Miu",boton_miu)
print("href de todos los <img>: ", imagenes)
print("Contador <a>: ", str(len(contadorA)))