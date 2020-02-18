#!/usr/bin/env python
# coding: utf-8

import requests
import json
import pandas as pd

url ='https://u3b6gr4ua3-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia%20for%20vanilla%20JavaScript%20(lite)%203.22.1%3BJS%20Helper%202.20.1&x-algolia-application-id=U3B6GR4UA3&x-algolia-api-key=9a20c93440cf63cf1a7008d75f7438bf'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'}

params = {
'x-algolia-agent': 'Algolia for vanilla JavaScript (lite) 3.22.1;JS Helper 2.20.1',
'x-algolia-application-id': 'U3B6GR4UA3',
'x-algolia-api-key': '9a20c93440cf63cf1a7008d75f7438bf'}

data = {"requests":[{"indexName":"noa_aem_game_en_us","params":"query=&hitsPerPage=42&maxValuesPerFacet=30&page=0&tagFilters="}]}
jsondata = json.dumps(data)

jsonObj = requests.post(url, data=jsondata, params=params).json()

## Extract Data and storing to Data frame 
game_670 = []
for each in jsonObj['results'][0]['hits']:
        game_670.append({'Game Title' : each['title'],
                     'Availability' : str(each['availability']).replace('[','').replace(']',''),
                     'Game url' : each['url'],'slug' : each['slug'],
                     #'Game Price $' : each['msrp'],
                     #'PlatForm' : each['platform'],
                     'Game Character' : str(each['characters']).replace('[','').replace(']',''),
                     'Categories' : str(each['categories']).replace('[','').replace(']',''),
                     #'Esrb  Ratings by' : each['esrb'],
                     'Virtual Console' : each['virtualConsole'],
                     'General Filters' : str(each['generalFilters']).replace('[','').replace(']',''),
                     'Filter Shop' : str(each['filterShops']).replace('[','').replace(']',''),
                     'Filterplayers' : str(each['filterPlayers']).replace('[','').replace(']',''),
                     #'publisher' : str(each['publishers']).replace('[','').replace(']',''),
                     #'Developers' : str(each['developers']).replace('[','').replace(']',''),
                     'No of Players' : each['players'],
                     'Featured' : each['featured'],
                     'free to start' : each['freeToStart'],
                     'Object ID' : each['objectID'],
                     'Game Discription' : each['description']
                })
    
game_1000 = []
for each in jsonObj['results'][0]['hits']:
    try:
        game_1000.append({'Game Title' : each['title'],
                     'Availability' : str(each['availability']).replace('[','').replace(']',''),
                     'Game url' : each['url'],
                     'slug' : each['slug'],
                     'Game Price ' : each['msrp'],
                     'PlatForm' : each['platform'],
                     'Game Character' : str(each['characters']).replace('[','').replace(']',''),
                     'Categories' : str(each['categories']).replace('[','').replace(']',''),
                     'Esrb Ratings by' : each['esrb'],
                     'Virtual Console' : each['virtualConsole'],
                     'General Filters' : str(each['generalFilters']).replace('[','').replace(']',''),
                     'Filter Shop' : str(each['filterShops']).replace('[','').replace(']',''),
                     'Filterplayers' : str(each['filterPlayers']).replace('[','').replace(']',''),
                     'Publisher' : str(each['publishers']).replace('[','').replace(']',''),
                     'Developers' : str(each['developers']).replace('[','').replace(']',''),
                     'No of Players' : each['players'],
                     'Featured' : each['featured'],
                     'free to start' : each['freeToStart'],
                     'Object ID' : each['objectID'],
                     'Game Discription' : each['description']
                })
    except:
        pass


## storing Data to Dataframe    
    
games_data_670 = pd.DataFrame(game_670)
games_data_1000 = pd.DataFrame(game_1000)
games_data_1000.to_csv(r'games_data_1000.csv')
games_data_670.to_csv(r'games_data_670.csv')
