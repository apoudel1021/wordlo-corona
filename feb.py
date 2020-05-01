# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 23:47:24 2020

@author: deadp
"""

from bs4 import BeautifulSoup
import urllib
import time 
from selenium import webdriver 

start_time = time.time()

driver = webdriver.Chrome()

driver.get("https://www.worldometers.info/coronavirus/feb-2020-news-updates-covid19/")

soup = BeautifulSoup(driver.page_source,'html.parser')

process=soup.body.find('div',class_='content-inner')

newstext = process.findAll('li')
text=[]
source =[]

process1=process.findAll('ul')

#print "Processing the first loop"
#
for u in process1:
    newstext= u.findAll('li')
    singletext=[]
    for i in range(len(newstext)):
#        print newstext[i]
        text.append(newstext[i].text)
        
        clink= newstext[i].findAll('a')
        seplink=[]
        for c in range(len(clink)):
            links= clink[c].get('href')
            seplink.append(links)
        source.append(seplink)
print len(text)

print len(source)

print text[0]
print source[0]
#print text

import pandas as pd 
test_df =pd.DataFrame({'Text':text,'Source':source})


test_df.to_csv('coronafebwithduppli.csv',sep=",", encoding='utf-8', index=False)   

data = pd.read_csv('coronafebwithduppli.csv')
orig = data.drop_duplicates(keep='first')
orig.to_csv('coronafeb.csv',sep=",", encoding='utf-8', index=False) 
print("--- %s seconds ---" % (time.time() - start_time))
