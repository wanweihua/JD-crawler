#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup


def gethtml(url):
    r = requests.get(url)
    return r.content


def parsehtml(html):
    soup = BeautifulSoup(html, 'html.parser')
    body = soup.body
    shopname = body.find('div',attrs={'class':'seller-infor'})
    if shopname:
        the_shopname = shopname.a  # 商铺名称
        if the_shopname:
            return the_shopname['title']
        else:
            return '无'
    else:
        return '无'




URl = 'https://item.jd.com/2680178.html'
html = gethtml(URl)
parsehtml(html)
# parsehtml(html)return的信息为商铺名称（若没有商铺名称则为‘无’）