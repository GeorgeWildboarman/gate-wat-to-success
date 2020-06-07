


from bs4 import BeautifulSoup

fm = 'bocchan-html.txt'
f = open(fm, "rt")
html = f.read()
f.close()

soup = BeautifulSoup(html,'html.parser')
#print(soup)

#print(soup.find('div',class_=["bibliographical_information","notation_notes"]))
#print(soup.find_all('div'))

rm = soup.find_all('div',class_=["bibliographical_information","notation_notes"])
for element in rm:
    element.extract()

rm = soup.find_all('rp')
for element in rm:
    element.extract()

rm = soup.find_all('rt')
for element in rm:
    element.extract()

#print(soup)
print(soup.get_text())

#print(soup.prettify())
#print(soup.a)
#print(soup.find_all('a'))
#print(soup.p)
#print(soup.ruby)

'''
import re
s = 'foo1\nfoo2\n   foo3\n allfoo\n hellofoo\n gofoo\n'
print(s)
result=re.search('foo.',s)
print(result)
result=re.search('foo',s)
print(result)
result=re.findall('foo',s)
print(result)
result=re.findall('foo.',s)
print(result)
'''
