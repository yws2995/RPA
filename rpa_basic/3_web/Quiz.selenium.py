from selenium import webdriver
import time
# 1. http://www.w3schools.com 접속
browser = webdriver.Chrome()
browser.maximize_window()
browser.get('https://www.w3schools.com/')

# 2. 화면 중간 LEARN HTML 클릭
browser.find_element_by_xpath('//*[@id="main"]/div[2]/div/div[1]/a[1]').click()

# 3. 상단 메뉴 중 HOW TO 클릭
browser.find_element_by_xpath('//*[@id="topnav"]/div/div/a[10]').click()

# 4. 좌측 메뉴 중 Contact Form 메뉴 클릭
# browser.find_elements_by_xpath('//*[@id="leftmenuinnerinner"]/a[117]').click()
# browser.find_elements_by_link_text('Contact FOrm').click() # Contact Form 이라는 2개 이상의 링크 텍스트가 있는 경우 실패
browser.find_element_by_xpath('//*[@id="leftmenuinnerinner"]/a[text()="Contact Form"]').click() # 가장 좋은 방법
# Contact 2020, 2019 등 매해 바뀔 때 일부 텍스트만 확인하려면
# browser.find_elements_by_xpath('//*[@id="leftmenuinnerinner"]/a[contains(text(), "Contact")]').click() # 가장 좋은 방법

# 5. 입력란에 아래 값 입력
#     First Name : 나도
#     Last Name : 코딩
#     Country : Canada
#     Subject : 퀴즈 완료하였습니다.
#     위 값들은 변수로 미리 저장해두세요
first_name = "나도"
last_name = "코딩"
country = "Canada"
subject = "퀴즈 완료하였습니다."

browser.find_element_by_xpath('//*[@id="fname"]').send_keys(first_name)
browser.find_element_by_xpath('//*[@id="lname"]').send_keys(last_name)
browser.find_element_by_xpath('//*[@id="country"]/option[text()="{}"]'.format(country)).click()
browser.find_element_by_xpath('//*[@id="main"]/div[3]/textarea').send_keys(subject)

# 6. 5초 대기 후 submit 버튼 클릭
time.sleep(5)
browser.find_element_by_xpath('//*[@id="main"]/div[3]/a').click()

# 7. 5초 대기 후 브라우저 종료
time.sleep(5)
browser.quit()