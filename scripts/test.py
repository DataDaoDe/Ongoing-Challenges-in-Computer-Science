import os
import marko
from bs4 import BeautifulSoup
import requests
from urllib.parse import urlparse

readme_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "README.md")

with open(readme_path, "r") as f:
    data = f.read()

html_data = marko.convert(data)
soup = BeautifulSoup(html_data, "html.parser")

# test all links
for link in soup.find_all('a', href=True):
    challenge_href = link['href']
    url = urlparse(challenge_href)
    response = requests.get(challenge_href)
    if response.status_code != 200:
        print(response.status_code, challenge_href)
    