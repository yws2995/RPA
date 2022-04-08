import pyautogui

# 마우스 이동

# pyautogui.moveTo(100, 100) # 지정한 위치로 마우스를 이동
# pyautogui.moveTo(100,200, duration = 3) # 0.25 동안 100,200 위치로 이동

# pyautogui.moveTo(100,100, duration = 0.25)
# pyautogui.moveTo(200,200, duration = 0.25)
# pyautogui.moveTo(300,300, duration = 0.25)

# 상대 좌표로 이동 ( 현재 커서가 있는 위치로부터 )
# pyautogui.moveTo(100, 100, duration = 0.25) # 지정한 위치로 마우스를 이동
# print(pyautogui.position()) # point(x,y)
# pyautogui.move(100,100,duration = 0.25)
# print(pyautogui.position()) # point(x,y)
# pyautogui.move(100,100,duration = 0.25)
# print(pyautogui.position()) # point(x,y)

p = pyautogui.position()
print(p[0], p[1])
print(p.x, p.y)

