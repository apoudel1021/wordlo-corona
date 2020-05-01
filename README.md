# wordlo-corona
Wordlo-corona collects all the updates and their respective sources of a given date as displayed on the website [https://www.worldometers.info/coronavirus/] making use of web scraping tool: Selenium.

This program runs on Python 3.7 and can be used in collecting data passing the valid parameters.

For example: In the website worlometer, you have acess to data with the cases for 6 days. After that you can either do View more News or get the archived data. 

In worldometer.py, you will be able to crawl the data for those 6 specific days passing the valid parameter. 

For example in the image below:

If you use this condition, you will get a csv file with 2 columns [Text, Source]. 
```python
for i in range(30,26,-1)
```
However, if you wish to crawl all the archived data, you can run feb.py!

feb.py provides you with all the archived data of February. [https://www.worldometers.info/coronavirus/feb-2020-news-updates-covid19/]

Happy Scraping! 
