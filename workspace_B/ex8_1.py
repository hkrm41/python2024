from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome()
driver.get("https://www.naver.com")
driver.implicitly_wait(0.5)
query_text=f'영화 파묘 누적 관객수'
search_box=driver.find_element(by=By.CSS_SELECTOR,value='#query')
search_box.send_keys(query_text)
search_butont=driver.find_element(by=By.CSS_SELECTOR,value='#search-btn')
search_butont.click()
temp_div=driver.find_element(by=By.CSS_SELECTOR,value="#main_pack > div.sc_new.cs_common_module.case_empasis.color_6._au_movie_content_wrap > div.cm_content_wrap > div.cm_content_area._cm_content_area_info > div > div.custom_info_wrap > div > div > div:nth-child(1) > div > div")
print("20121 이장혁")
print(temp_div.text)
time.sleep(10)
