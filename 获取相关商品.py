# -*- coding: utf-8 -*-


import requests
from bs4 import BeautifulSoup


def gethtml(url):
    r = requests.get(url)
    return r.content


def parsehtml(html):
    soup = BeautifulSoup(html, 'html.parser')
    body = soup.body
    data = body.find('div', attrs={'id': 'related-brands'})
    goodslist = data.find('ul')
    for li in goodslist.find_all('li'):
        name = li.get_text()  #获取相关商品名称
        href = li.a['href']   #获取相关商品链接
        return name,'http:'+href


URl = 'https://item.jd.com/2680178.html'
html = gethtml(URl)
parsehtml(html)

#parsehtml(html)中return的信息为(相关商品名称，获取相关商品链接)