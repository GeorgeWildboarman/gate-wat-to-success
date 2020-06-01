
import requests
url='https://www.aozora.gr.jp/cards/000148/files/752_14964.html'
f=requests.get(url)
f.encoding=f.apparent_encoding
#f.encoding='utf-8'
#print(f.text)
print(f.encoding)
#print(f.content)
fw=open("bocchan-html.txt", "wt")
fw.write(f.text)
fw.close()




