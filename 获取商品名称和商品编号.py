# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup


def gethtml(url):
    r = requests.get(url)
    return r.content


def parsehtml(html):
    soup = BeautifulSoup(html,'html.parser')
    body = soup.body

    data1 = body.find('div', attrs={'id': 'product-detail'})



    parameter1 = data1.find('div', attrs={'id': 'product-detail-2'})
    parameter2 = data1.find('div', attrs={'class': 'p-parameter'})
    if parameter2:
        goods_introduction =  parameter2.get_text()  # 商品介绍
    else:
        goods_introduction = '无'
    if parameter1:
        goods_parameter = parameter1.get_text()  # 商品参数
    else:
        goods_parameter = '无'

    return goods_introduction,goods_parameter

url = 'https://item.jd.com/2680178.html'
html = gethtml(url)
parsehtml(html)
#parsehtml(html)return的信息为（商品介绍，商品参数）