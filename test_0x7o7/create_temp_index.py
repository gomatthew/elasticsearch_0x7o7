# -*- coding: utf-8 -*-
import pymysql
import elasticsearch
es = elasticsearch.Elasticsearch(hosts='http://127.0.0.1:19200')
conn = pymysql.connect(host='127.0.0.1',user='root',password='makemoney',charset='utf8',database='spider')
cur = conn.cursor(cursor=pymysql.cursors.DictCursor)

cur.execute('''select * from comment_detail limit 1;''')
res = cur.fetchone()
conn.close()
es.index(index='test',id=res.get('id'),document=res)