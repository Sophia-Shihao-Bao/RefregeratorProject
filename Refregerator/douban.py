#encoding= 'utf-8'
import requests
from bs4 import BeautifulSoup
import os
userimput = input('请输入您要搜索的蔬菜材料，若多个，请拿加号：+ 连接')
url = "https://www.xiachufang.com/search/?keyword="+userimput+"&cat=1001"
headers = headers = {   # 请求头文件
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:57.0) Gecko/20100101 Firefox/57.0',
            'Upgrade-Insecure-Requests':'1',
            'Host':'www.xiachufang.com',
            'Cookie':'bid=kQ82GDsK; gr_user_id=b6c4ae54-136a-45f2-a497-ad9131dff47a; __utma=177678124.392935892.1511776434.1511776434.1511776434.1; __utmz=177678124.1511776436.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); Hm_lvt_ecd4feb5c351cc02583045a5813b5142=1511776486,1511942546; gr_session_id_8187ff886f0929da=595c7891-62df-44e1-a71a-ba6f482a200b; Hm_lpvt_ecd4feb5c351cc02583045a5813b5142=1511942570',
            'Connection':'keep-alive',
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Encoding':'gzip, deflate',
        }

content = requests.get(url = url, headers=headers)
soup = BeautifulSoup(content.content,'lxml')
name = soup.find_all('p', class_='name')
count = 1
recipeMenu = []
for i in name:
    title = i.find_all('a')
    titleLink = title[0].get('href')
    recipeMenu.append(titleLink)
    #print(titleLink)
    foodname = i.text
    print(str(count)+'.',end='')
    for m in foodname:
        if (m!=' ' and m!= '\n'):
            print(m,end=' ')
    print()
    count = count+1

userimput2 = input('请输入您要要查的数学编号（不要打"。"）')
code = recipeMenu[int(userimput2)-1]

url2 = "https://www.xiachufang.com/"+ code
content2 = requests.get(url2, headers = headers)
soup2 = BeautifulSoup(content2.content,'lxml')
#steps = soup2.find_all('a')
howmuch = soup2.find_all('p', class_ = 'text')
material = soup2.find_all('td', class_ = 'name')
for i in howmuch:
    print(i.text)


#print(steps)
#print(howmuch)