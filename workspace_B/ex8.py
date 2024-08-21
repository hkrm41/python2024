from selenium import webdriver #pip install selenium
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.get("https://time.navyism.com/?host=www.naver.com")
driver.implicitly_wait(0.5)
message=driver.find_element(by=By.ID, value="time_area")
print(message.text)
while True:
    message=driver.find_element(by=By.ID, value="time_area")
    print(message.text)
    if message.text=="2024년 04월 02일 13시 53분 42초":
        break
print("시간 끝")
time.sleep(10)
