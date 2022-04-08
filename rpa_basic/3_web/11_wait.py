# 특정 웹사이트에서는 한동안 기다려야 하는 경우가 있다.
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_condition as EC

browser = webdriver.Chrome()
browser.maximize_window()
browser.get('https://flight.naver.com/')
# 가는 날
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]').click()
time.sleep(1)
browser.find_elements_by_link_text('25')[0].click()
#오는 날 
browser.find_elements_by_link_text('5')[1].click()

# 첫 번째 여행지 클릭
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[7]/div/div[2]/div/ul/li[1]/button/figure/img').click()

# 항공권 검색 클릭
browser.find_elements_by_link_text('항공권 검색').click()

# time.sleep(10)

try:
    elem = WebDriverWait(browser,10).until(EC.presence_of_element_located((By.XPATH, '~~')))
    print(elem.text)
except: 
    print("실패했어요")

# 첫 번째 결과 출력
# elem = browser.find_element_by_xpath('~~')
# print(elem.text) # element 내에 있는 text 부분을 출력

time.sleep(5)
browser.quit()