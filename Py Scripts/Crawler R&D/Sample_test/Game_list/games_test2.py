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

## storing data 
all_data=jsonObj['results'][0]['hits']

## storing Data to Dataframe    
    
all_data_df = pd.DataFrame(all_data)

all_data_df.to_csv(r'games_data_df.csv')

