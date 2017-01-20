# -*- coding: utf-8 -*-



import requests
import json
#修改url中的referenceIds即可
url = 'https://club.jd.com/comment/productCommentSummaries.action?referenceIds=2680178'

#获取html
def get_html(url):
    return requests.get(url).content

#转化为json解析
def parse_html(html):
    html = html.decode('GBK')            #转码
    json_data =json.loads(html)
    dict = json_data['CommentsCount'][0]

    CommentCount = dict['CommentCount']   #评论数量
    GoodRate =dict['GoodRate']            #好评率
    PoorRate = dict['PoorRate']           #差评率
    GeneralRate = dict['GeneralRate']     #一般率
    average_score = dict['AverageScore']  # 平均评分
    return  CommentCount, GoodRate, PoorRate,GeneralRate,average_score


html = get_html(url)
parse_html(html)
# parse_html(html)返回的为（评价数量，好评率，差评率，一般率， 平均评分）
