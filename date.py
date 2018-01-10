import  pandas as pd
import json
from pprint import pprint 
import codecs
from datetime import datetime, timedelta

data = json.load(codecs.open('Movie-2017.json', 'r', 'utf-8'))

movie_date = '2017/8/23'
movie_date = datetime.strptime(movie_date, '%Y/%m/%d')

poi = []
keyword = ['模犯生']

for movie in data['articles']:
    try:
        article_date = datetime.strptime(movie['date'], '%a %b %d %H:%M:%S %Y')
    except:
        try:
            article_date = datetime.strptime(movie['date'], '%Y/%m/%d %H:%M:%S')
        except:
            continue
    if movie['article_title'] and article_date <= movie_date and article_date >= movie_date - timedelta(days=180):
        if keyword[0] in movie['article_title']:
            poi.append(movie)
        """
        if keyword[1] in movie['article_title']:
            if movie not in poi:
                poi.append(movie)
        """
push = 0
bad = 0
other = 0

for mv in poi:
    for message in mv['messages']:
        if message['push_tag'] == '推':
            push += 1
        elif message['push_tag'] == '噓':
            bad += 1
        else:
            other += 1

print(push, bad, other)
"""
from datetime import datetime, timedelta

article_date = datetime.strptime(poi[3]['date'], '%a %b %d %H:%M:%S %Y')
print(article_date)
movie_date = '2016/12/23'
movie_time = datetime.strptime(movie_date, '%Y/%m/%d')

print(movie_time>article_date - timedelta(days=180))
"""




