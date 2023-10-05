import requests
from bs4 import BeautifulSoup

url = "https://www.rcpit.ac.in"
req = requests.get(url)
soup = BeautifulSoup(req.content, "html.parser")
print(soup.get_text())

