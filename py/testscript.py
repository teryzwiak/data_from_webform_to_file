from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import re

req = requests.get('https://eskarbonka.wosp.org.pl/gikygofudy?fbclid=IwAR3OoVjyApMU8eTr-VjMfJlbezY2v5qy-Ng0HpOliGpVThqS2ew9QX5aKPo')
soup = BeautifulSoup(req.content, "html.parser")
start = soup.find("div", {"class": "col-md-10 mx-auto py-3 fs-2 fw-bold text-center bg-white price rounded-pill"})
start = str(start)
pattern = "<span.*?>.*?</span.*?>"
match_results = re.search(pattern, start, re.IGNORECASE)
title = match_results.group()
title = re.sub("<.*?>", "", title)
title = re.sub("zł", "", title)
money = int(title)
print(money)
data = { "number": money}
response = requests.post("plik.php", params=data)
plik.php