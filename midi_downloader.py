import requests
from bs4 import BeautifulSoup
import urllib
from os.path import dirname, join, realpath

save_loc = join(dirname(realpath(__file__)), "mids")

url = "https://bushgrafts.com/midi/"
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, "html.parser")

urls = []
for link in soup.find_all("a"):
    if ".mid" in str(link.get("href")).lower():
        # print(link.get("href"))
        urls.append(str(link.get("href")))

for u in urls:
    filename = str(urls.index(u)) + ".mid"
    urllib.request.urlretrieve(u, join(save_loc, filename))