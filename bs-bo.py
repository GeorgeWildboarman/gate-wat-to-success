from bs4 import BeautifulSoup

fm = 'bocchan-html.txt'
f = open(fm, "rt")
html = f.read()
f.close()

print(html)

