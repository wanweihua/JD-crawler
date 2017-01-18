#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 导入所需的开发模块
import requests
import re

# 创建循环链接
urls = []
for i in list(range(1,100)):
    urls.append('https://rate.tmall.com/list_detail_rate.htm?itemId=16204910274&spuId=269137423&sellerId=880734502&order=3&currentPage=3%s' %i)

# 构建字段容器
comment=[]

# 循环抓取数据
for url in urls:
    content = requests.get(url).text

# 借助正则表达式使用findall进行匹配查询
    comment.extend(re.findall('"rateContent":"(.*?)"',content))

for li in range(1,len(comment)):
    print comment[li]