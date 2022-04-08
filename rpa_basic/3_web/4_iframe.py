import time
from selenium import webdriver
browser = webdriver.Chrome()
browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_radio')

browser.switch_to.frame('iframeResult') #frame 전환

elem = browser.find_element_by_xpath('//*[@id="html"]')

# 선택이 안되어 있으면 선택하기
if elem.is_selected() == False: #라디오 버튼이 선택되어 있지 않으면
    elem.click()
else:
    print("이미 선택되어 있음")


time.sleep(5)


if elem.is_selected() == False: #라디오 버튼이 선택되어 있지 않으면
    elem.click()
else:
    print("이미 선택되어 있음")

