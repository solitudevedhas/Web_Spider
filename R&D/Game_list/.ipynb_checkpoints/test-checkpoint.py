import requests
import json

url ='https://u3b6gr4ua3-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia%20for%20vanilla%20JavaScript%20(lite)%203.22.1%3BJS%20Helper%202.20.1&x-algolia-application-id=U3B6GR4UA3&x-algolia-api-key=9a20c93440cf63cf1a7008d75f7438bf'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'}

params = {
'x-algolia-agent': 'Algolia for vanilla JavaScript (lite) 3.22.1;JS Helper 2.20.1',
'x-algolia-application-id': 'U3B6GR4UA3',
'x-algolia-api-key': '9a20c93440cf63cf1a7008d75f7438bf'}

data = {"requests":[{"indexName":"noa_aem_game_en_us","params":"query=&hitsPerPage=42&maxValuesPerFacet=30&page=0&tagFilters="}]}
jsondata = json.dumps(data)

jsonObj = requests.post(url, data=jsondata, params=params).json()

# print(jsonObj['results'][0])
c=1
for each in jsonObj['results'][0]['hits']:
    print (each['title'])
    print (each['releaseDateMask'].split('T')[0])
    try:
    	print (each['msrp'])
    except:
		pass

    print c,"\n"
    c+=1