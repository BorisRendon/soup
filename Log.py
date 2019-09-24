from bs4 import BeautifulSoup
import requests,sys,csv,json,re
import logs

soup = BeautifulSoup(r.content, "html.parser")

logs = open("logs/logs.text","w+")