from urllib.request import urlopen

url = "https://eskarbonka.wosp.org.pl/gikygofudy?fbclid=IwAR3OoVjyApMU8eTr-VjMfJlbezY2v5qy-Ng0HpOliGpVThqS2ew9QX5aKPo"

page = urlopen(url)

page

html_bytes = page.read()
html = html_bytes.decode("utf-8")

print(html)