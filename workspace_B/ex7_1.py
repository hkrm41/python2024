import requests
from bs4 import BeautifulSoup
ymd=input("원하는 급식 날짜 입력(20240327):")
url=f"https://school.use.go.kr/eonyang-h/M01030601/list?ymd={ymd}"
response=requests.get(url)
# print(response.text)
soup=BeautifulSoup(response.text,'html.parser') #분석도구
result=soup.find("a",href=f"/eonyang-h/M01030601/list?ymd={ymd}")
print("20121 이장혁")
print(result.text)