#---------------------------------------------------
#  Get the website - using HTTP library (Requests)
#---------------------------------------------------
import requests

html = requests.get("https://keithgalli.github.io/web-scraping/example.html")

print(html.content)
# ---Result from requests.get---
# C:\Users\HP\anaconda3\lib\site-packages\requests\__init__.py:89: RequestsDependencyWarning: urllib3 (1.26.7) or chardet (3.0.4) doesn't match a supported version!
#  warnings.warn("urllib3 ({}) or chardet ({}) doesn't match a supported "
# b'<html>\n<head>\n<title>HTML Example</title>\n</head>\n<body>\n\n<div align="middle">\n<h1>HTML Webpage
# </h1>\n<p>Link to more interesting example: <a href="https://keithgalli.github.io/web-scraping/webpage.html">keithgalli.github.io/web-scraping/webpage.html
# </a></p>\n</div>\n\n<h2>A Header
# </h2>\n<p><i>Some italicized text</i></p>\n\n
# <h2>Another header
# </h2>\n<p id="paragraph-id">
# <b>Some bold text</b></p>\n\n</body>\n</html>\n'


#--------Print URL--------------
print('Response url:', html.url)
# Response url: https://keithgalli.github.io/web-scraping/example.html


#-------Print Status Code-------------
print('Response status:', html.status_code)
# Response status: 200


#-------Print Encoding type-----------
print('Response status:', html.encoding)
# Response status: utf-8


#-------Print HTML Details-------------
print('Response headers:', html.headers)
# Response headers: {
# 'Connection': 'keep-alive', 
# 'Content-Length': '259', 
# 'Server': 'GitHub.com', 
# 'Content-Type': 'text/html; charset=utf-8', 
# 'permissions-policy': 'interest-cohort=()', 
# 'Last-Modified': 'Fri, 03 Jul 2020 00:21:07 GMT', 
# 'Access-Control-Allow-Origin': '*', 
# 'ETag': 'W/"5efe79f3-198"', 
# 'expires': 'Sat, 27 Nov 2021 07:41:09 GMT', 
# 'Cache-Control': 'max-age=600', 
# 'Content-Encoding': 'gzip', 
# 'x-proxy-cache': 'MISS', 
# 'X-GitHub-Request-Id': 'E580:2FED:3D2033:4453B6:61A1DEBD', 
# 'Accept-Ranges': 'bytes', 
# 'Date': 'Sat, 27 Nov 2021 08:38:15 GMT', 
# 'Via': '1.1 varnish', 
# 'Age': '146', 
# 'X-Served-By': 'cache-qpg1267-QPG', 
# 'X-Cache': 'HIT', 
# 'X-Cache-Hits': '1', 
# 'X-Timer': 'S1638002296.514192,VS0,VE0', 
# 'Vary': 'Accept-Encoding', 
# 'X-Fastly-Request-ID': '80e9b676c0af1f4211ec035920c72532a553807a'}
#-----------------------------------------------------------------




