from bs4 import BeautifulSoup
import requests
url = "https://www.econocom.com"
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")
for link in soup.find_all('a'):
    print(link.get('href'))
    print(soup.title)


 # Output <title>Econocom | As-a-service Solutions For Digital Transformation Projects</title>