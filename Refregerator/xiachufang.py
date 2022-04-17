import requests
from bs4 import BeautifulSoup
import os

for page in range(1,2):
    url = 'https://m.xiachufang.com/recipe/105969665/'
    #print("now at web:"+str(url))
    content = requests.get(url)
    soup = BeautifulSoup(content.content,'lxml')
    name = soup.find_all('h1', class_ ='recipe-name tc')
    #print(name)

    for text in name:
        title = text.get('data-v-d3a34eca')#url
        #with open(title+os.path.splitext(text)[-1],'wb')as f:
            #img = requests.get(text).content
            #f.write(img)
print(content)
print(name)
