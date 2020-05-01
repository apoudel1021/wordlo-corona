# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 14:59:02 2020

@author: deadp
"""

import time 
from bs4 import BeautifulSoup
#import urllib 

from selenium import webdriver 

start_time = time.time()
#


text = []
source =[]

driver = webdriver.Chrome()

driver.get("https://www.worldometers.info/coronavirus/")

soup = BeautifulSoup(driver.page_source,'html.parser')

for i in range(29,23,-1):
    if i>=10:
        j = 'newsdate2020-04-'+str(i)
    else:
        j = 'newsdate2020-04-0'+str(i)
        
    print j
    
    print "***************************"

    process = soup.body.find(id=j)
    print process
    
    allposts = process.findAll('div',class_='news_post')

#    print process
    print  " #####################"
    
#    print len(allposts)
    
    print "Running for loop"
    for i in range(len(allposts)):
        
        try:
            newstext= allposts[i].div.ul.li.text
        except:
            newstext= allposts[i].div.text
        
        seplink = []
        links = allposts[i].findAll('a')
        for link in range(len(links)):
            
            clink = links[link].get('href')
            seplink.append(clink)
        
        source.append(seplink)
        
        
    #        
        text.append(newstext)
        
print len(source)
print len(text)
#print source 
#print text 

import pandas as pd 
test_df =pd.DataFrame({'Text':text, 'Source':source}) 
print test_df

test_df.to_csv('april20-15.csv',sep=",", encoding='utf-8', index=False)    
print("--- %s seconds ---" % (time.time() - start_time))

print 'end'


