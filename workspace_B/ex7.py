import requests
from bs4 import BeautifulSoup
url="https://www.aladin.co.kr/home/welcome.aspx"
response=requests.get(url)
# print(response.text)
soup=BeautifulSoup(response.text,'html.parser') #분석도구
result=soup.select(".sub")
print(len(result))
for r in result:
    print(r.text)