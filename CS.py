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

#  GET following <meta>: "title", "description" ("og")

#count all <a>
ContadorA = soup.findAll('a')
#Count all <div>
ContadorDiv = soup.findAll('div')

#Prints
print("Titulo CS: \n" , soup.title.string)
#print("Href: \n" , href)
print("Contador de <a>:\n ", str(len(ContadorA)))
print("Contador de <div>:\n", str(len(ContadorDiv)))