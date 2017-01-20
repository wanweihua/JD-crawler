# -*- coding: utf-8 -*-
import requests
import json
#修改url中的productIdhe和page数目,即可

url = 'https://sclub.jd.com/comment/productPageComments.action?productId=2680178&score=0&sortType=3&page=0&pageSize=10'

#获取html
def get_html(url):
    return requests.get(url).content

#转化为json解析
def parse_html(html):
    html = html.decode('GBK')            #转码
    json_data =json.loads(html)
    comment_list = json_data['comments']

    infor = []
    for i in range(len(comment_list)):
        list = comment_list[i]
        comment =  list['content']#
        id = list['id']#用户id
        creationTime =list['creationTime']#评论时间
        userClientShow = list['userClientShow']#使用客户端
        userLevelName = list['userLevelName']#用户等级


html = get_html(url)
parse_html(html)
