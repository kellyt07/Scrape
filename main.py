from bs4 import BeautifulSoup
import requests

url = input("Enter a URL:")

r = requests.get("http://" + url)

data = r.text;

soup = BeautifulSoup(data, "html.parser");

for link in soup.findAll('a'):
    print(link.get("href"))