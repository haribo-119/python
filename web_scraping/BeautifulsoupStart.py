from bs4 import BeautifulSoup
import urllib.request as req



def getMeals(date='0127'):
    baseURL = 'https://school.cbe.go.kr/cbs-h/M01050705/list?ymd=2025'
    headers = {'User-Agent': 'Mozilla/5.0'}
    request = req.Request(baseURL+date,headers=headers)

    res = req.urlopen(request)
    soup = BeautifulSoup(res,'html.parser')
    meals=soup.find_all(class_='tch-lnc-wrap')
    dic = {}

    for meal in meals :
        dic.update({meal.dt.text:meal.ul.text})
    return dic    
  
print(getMeals('0131'))