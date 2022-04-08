import pyautogui
# pyautogui.FAILSAFE = False # 어떤 경우에도 끝까지 동작하게 하는데 추천하지는 않는 방법이다
pyautogui.PAUSE = 1 # 모든 동작에 1초씩 sleep을 적용
# pyautogui.mouseInfo() ##자주 쓰게 될 것 여러가지 인포메이션

# 작업 중 중단해야 할 때는 마우스를 귀퉁이로 보내버린다. 
for i in range(10):
    pyautogui.move(100,100)
