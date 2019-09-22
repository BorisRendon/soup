from bs4 import BeautifulSoup
import requests,sys,csv,json

url = "http://ufm.edu/Portal"
source = requests.get(url)
plain_text = source.content
soup = BeautifulSoup(plain_text, "lxml")
links = soup.findAll('a', {'class': 'a-link-normal s-access-detail-page a-text-normal'})
print(len(links))
for link in links:
    title = link.get('Title')
    print(title)