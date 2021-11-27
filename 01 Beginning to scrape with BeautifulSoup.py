#-------------------------------------------------------------------
#-------------Beginning to scrape with BeautifulSoup----------------
#-------------------------------------------------------------------
# ****Scraping text****

import requests
from bs4 import BeautifulSoup

html = requests.get("https://keithgalli.github.io/web-scraping/example.html")
bs = BeautifulSoup(html.content, "html.parser")

print(bs.prettify())


#----------------find() and find_all() with BeautifulSoup-----------

result_find = bs.find('h2')
result_findall = bs.find_all('h2')

print('find: ', result_find)
print('find_all: ', result_findall)
# find:  <h2>A Header</h2>
# find_all:  [<h2>A Header</h2>, <h2>Another header</h2>]


#------------------Print Header(h1, h2)-------------------------------
result_header_tags = bs.find_all(['h1', 'h2','h3','h4','h5','h6'])
print('Header: ', result_header_tags)
# Header:  [<h1>HTML Webpage</h1>, <h2>A Header</h2>, <h2>Another header</h2>]


#---------------Print Details(p)--------------------------------
result_p_tags = bs.find_all('p')
print('p: ', result_p_tags)
# p:  [<p>Link to more interesting example: <a href="https://keithgalli.github.io/web-scraping/webpage.html">keithgalli.github.io/web-scraping/webpage.html</a></p>, 
#      <p><i>Some italicized text</i></p>, 
#      <p id="paragraph-id"><b>Some bold text</b></p>]


#-----------Scrap only text in p--------------------------------
for tag in result_p_tags:
    print(tag.get_text())
# Link to more interesting example: keithgalli.github.io/web-scraping/webpage.html
# Some italicized text
# Some bold text

#----------Select one p by id(last)--------------------------
result_p_by_id = bs.find('p', attrs={'id': 'paragraph-id'})
print(result_p_by_id.get_text())
# Some bold text

#----------------------------------------------------------------