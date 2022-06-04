
import requests
from bs4 import BeautifulSoup
from flask import request
url="https://amigurum.com/"


headers={
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
}
resp=requests.get(url,headers=headers)
body=resp.content
soup=BeautifulSoup(body,features="lxml")

#scraping
categories=soup.find_all("p",{"class":"post-category"})
post_date=soup.find_all("p",{"class":"post-date"})
entry_info=soup.find_all("div",{"class":"entry excerpt entry-summary"})


#crawling 
#links=[l.attrs["href"] for l in soup.find_all] 
links=set(soup.find_all("a",{"class":"external"}))
visited_links=set([url])
queue=set()
queue=links-visited_links
for el in queue:
	print(el['href'])


#for p in categories:
#	div=p.text.strip()
#	print(div)
