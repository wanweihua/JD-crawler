
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import csv
import codecs



def get_html(url):
    return requests.get(url).content

def parse_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    body = soup.body
    clearfix= body.find('div',attrs={'class','grid-16-8 clearfix'})
    article = clearfix.find('div',attrs={'class','article'})
    table = article.find_all('div',attrs={'class','pl2'})
    author = article.find_all('p',attrs={'class','pl'})
    for li in table:

        name.append(li.get_text().encode('utf-8'))
        href.append(li.a['href'].encode('utf-8'))
    for mi in author:
        text.append(mi.get_text().encode('utf-8'))
url_list =[]
page = 'https://book.douban.com/top250'
for num in range(0,275,25):

    url_list.append(page+'?start='+str(num))
name = []
href = []
text = []

for url in url_list:
    html = get_html(url)
    parse_html(html)










