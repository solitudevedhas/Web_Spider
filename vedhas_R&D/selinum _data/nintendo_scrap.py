## import required packages
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import selenium.webdriver.support.ui as ui
import selenium.webdriver.support.expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd
import os
import time

options = webdriver.ChromeOptions() ## calling chrome webdriver class options
driver = webdriver.Chrome(options=options,executable_path='chromedriver.exe')
driver.get("https://www.nintendo.com/games/game-guide/#filter/:q=")


## load more 
while True:
    try:
        elm = driver.find_element_by_tag_name('#btn-load-more')
        #elm.send_keys(Keys.END)
        time.sleep(2)
        elm.click()
        time.sleep(5)
    except Exception as e:
        print(e)
        break
print ("Complete")
time.sleep(10)

game_title=[] #List to store name of the games title
game_prices=[] #List to store price of the game prices 
game_relese=[] #List to store rating of the game release date


### extract info 
content = driver.page_source
soup = BeautifulSoup(content)
for a in soup.findAll('a',href=True, attrs={'class':'main-link'}):
    title = a.find('h3', attrs={'class':'b3'})
    price = a.find('p', attrs={'class':'b3 row-price'})
    release = a.find('p', attrs={'class':'b4 row-date'})
    game_title.append(title.text)
    game_prices.append(price.text)
    game_relese.append(release.text) 
    
game_data=pd.DataFrame({'Games Title': game_title, 'Games release': game_relese, 'Games Price': game_prices})
print(game_data)

game_data.to_csv(r'game_data.csv')

## 