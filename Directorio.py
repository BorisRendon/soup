from bs4 import BeautifulSoup
import requests,sys,csv,json
import urllib

url =  "https://www.ufm.edu/Directorio"
r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")
def directory():
    #sort all emails
    lista_email = []
    hrefs = soup.findAll(attrs ={'href': True})
    for x in hrefs:
        if 'mailito' in x['href']:
            lista_email.append(x['href'].split(':')[1])
    lista_email.sort()
    #contar email que comienze con vocal , solo mostrar la cuenta
    cuenta = 0
    vocales =  ('a','e','i','o','u')
    for i in lista_email:
        if lista_email[0].startswith(vocales):
            cuenta +=1
    










    print("BORIS RENDÓN")
    print("4. Directorio")
    print("Sort all emails alphabetically:\n",(repr(lista_email)))
    print("Cuenta de emails que comienzan con vocal:\n",cuenta)



