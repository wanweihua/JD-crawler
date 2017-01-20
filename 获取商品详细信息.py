# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

def gethtml(url):
    r = requests.get(url)
    return r.content


def parsehtml(html):
    soup = BeautifulSoup(html,'html.parser')
    body = soup.body
    data = body.find('div', attrs={'id': 'product-detail'})
    parameter1 = data.find('div', attrs={'id': 'product-detail-2'})
    parameter2 = data.find('div', attrs={'class': 'p-parameter'})
    goods_introduction = parameter2.get_text()   #商品介绍
    goods_parameter = parameter1.get_text()   #商品参数
    print goods_introduction
    print goods_parameter



URl = 'https://item.jd.com/2680178.html'
html = gethtml(URl)
parsehtml(html)