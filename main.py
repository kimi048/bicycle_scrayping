import requests
import csv
from bs4 import BeautifulSoup

response = requests.get('https://www.pasonatech.co.jp/')
baseURI="http://cycling-tomorrow.jp/bicycle_shop/"
ibaraki="http://www.cycling-tomorrow.jp/bicycle_shop/region/block_kanto/ibaraki/index.html"

res=requests.get(ibaraki)
s=BeautifulSoup(res.content,'html.parser')
soup = BeautifulSoup(response.text, 'html.parser')
title = soup.find('title').get_text()
cycletitle=s.select("article h1 a")
cyclebody1=s.select("article ul.indent_tight li:nth-child(1)")
cyclebody2=s.select("article ul.indent_tight li:nth-child(2)")
for num in range(10):
  print(cycletitle[num].text)
  print(cyclebody1[num].text)
  print(cyclebody2[num].text)
with open('./data.csv', 'w') as f:
    writer = csv.writer(f)
    for num in range(10):
      writer.writerow([cycletitle[num].text, cyclebody1[num].text, cyclebody2[num].text])
    #writer.writerow(['a', 'b', 'c'])
#page_body > div.grand_cols.clearfix > div.gc_center.archive_list > div > section > article:nth-child(4) > header > h1
#page_body > div.grand_cols.clearfix > div.gc_center.archive_list > div > section > article:nth-child(5)