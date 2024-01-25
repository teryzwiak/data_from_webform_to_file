from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import re

url = "https://eskarbonka.wosp.org.pl/gikygofudy?fbclid=IwAR3OoVjyApMU8eTr-VjMfJlbezY2v5qy-Ng0HpOliGpVThqS2ew9QX5aKPo"

#page = urlopen(url)

#page

#html_bytes = page.read()
#html = html_bytes.decode("utf-8")

#print(html)

req = requests.get('https://eskarbonka.wosp.org.pl/gikygofudy?fbclid=IwAR3OoVjyApMU8eTr-VjMfJlbezY2v5qy-Ng0HpOliGpVThqS2ew9QX5aKPo')
req
soup = BeautifulSoup(req.content, "html.parser")
start = soup.find('div')
start = start.find("price")
re.find()
print(start)