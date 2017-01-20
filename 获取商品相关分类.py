# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup


def gethtml(url):
    r = requests.get(url)
    return r.content


def parsehtml(html):
    soup = BeautifulSoup(html, 'html.parser')
    body = soup.body
    data = body.find('div', attrs={'id': 'related-sorts'})
    if data:
        relatedsort = data.get_text()
        return relatedsort     #其实就是商品相关分类
    else:
        return '无'





url = 'https://item.jd.com/2680178.html'
html = gethtml(url)
parsehtml(html)

#parsehtml（html）return的信息为商品相关分类（若没有则为‘无’）