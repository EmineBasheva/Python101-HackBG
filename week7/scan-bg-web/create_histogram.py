from histogram import Histogram
import requests
from bs4 import BeautifulSoup


headers = {}
headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2226.0 Safari/537.36'


histgr = Histogram()
r = requests.get('http://register.start.bg/', headers=headers)
mail_server = r.headers["Server"]
histgr.add(mail_server)

text_of_register = r.text
beu_text = BeautifulSoup(text_of_register)
# print(beu_text.prettify())

all_hrefs = []

for link in beu_text.find_all('a'):
    if not(link.get('href') is None) and link.get('href') != '#top':
        # print(link.get('href'))
        all_hrefs.append(link.get('href'))

print(len(all_hrefs))
# print(all_hrefs[27])

count_succes = 0

for href in all_hrefs:
    try:
        if 'http' not in href:
            link = 'http://register.start.bg/' + href
            req = requests.head(link, headers=headers, timeout=5)
            server = req.headers["Server"]
            histgr.add(server)
            print('-----', count_succes, link, req.status_code)
            count_succes += 1
        else:
            req = requests.head(href, headers=headers, timeout=5)
            server = req.headers["Server"]
            histgr.add(server)
            print('+++++', count_succes, link, req.status_code)
            count_succes += 1
            # print(count_succes, 'blaaaaa')
    except Exception:
        pass
    

print(count_succes)
# print(count, count_of_None)

print(histgr.get_dict())
