from bs4 import BeautifulSoup
import urllib.request as req

res = req.urlopen('http://127.0.0.1:5500/test/BeautifulsoupTest.html')
soup = BeautifulSoup(res,'html.parser')
# 리스트 형태로 가져옴
# print(soup.find_all('a'))

# 반복문을 통해 하나씩 가져옴옴
# for tag in soup.find_all('a'):
#     print(tag['href'])

# 자주 사용하게 되는 것
print(soup.select('body > div:nth-child(4) > img'))