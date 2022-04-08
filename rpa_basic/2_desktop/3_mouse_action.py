### 너무 빨라서 동작이 안되는 경우 가 잦기 떄문에 되도록 duration을 준다 ###

import pyautogui
pyautogui.sleep(3)
# print(pyautogui.position())

# pyautogui.click(1031,19, duration = 1) # 1초 이동 후 좌표 클릭
# pyautogui.click()
# 드래그에 활용
# pyautogui.mouseDown()
# pyautogui.mouseUp()

# pyautogui.doubleClick()
# pyautogui.click(clicks=2) # 더블클릭

# pyautogui.moveTo(200,200)
# pyautogui.mouseDown() # 마우스 버튼 누른 상태
# pyautogui.moveTo(200,300)
# pyautogui.mouseUp()
# pyautogui.rightClick()
# pyautogui.middleClick() # 마우스 휠

# pyautogui.moveTo(1114, 349)
# pyautogui.drag(100, 0) 

pyautogui.scroll(300) # 위 방향으로 300만큼 스크롤
# -300이면 아래 방향으로 300만큼 스크롤
