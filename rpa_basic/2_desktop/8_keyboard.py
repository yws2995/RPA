from pdb import line_prefix
import pyautogui
w = pyautogui.getWindowsWithTitle("제목 없음")[0] # 메모장 1개 띄운 상태에서 가져옴
w.activate() 

# pyautogui.write("12345")
# pyautogui.write("AAA", interval = 0.25)

# pyautogui.write("한글처리")

# pyautogui.write(["t","e","s","t","left","left","right","l","a","enter"], interval = 0.25)
# test 순서대로 적고 왼쪽 방향키 2번 오른쪽방향키 2번, l a 적고 enter 입력
# Automate the boring stuff with python 구글에 검색

# 특수 문자
# shift 4-> 5
# pyautogui.keyDown("shift") # shift 키를 누른 상태에서
# pyautogui.press("4") # 숫자 4를 입력하고
# pyautogui.keyUp("shift") # shift 키를 뗸다

# 조합키( Hot Key )
# pyautogui.keyDown("ctrl")
# pyautogui.keyDown("a")
# pyautogui.keyUp("a") # press("a")
# pyautogui.KeyUp("ctrl") # Ctrl + A

# pyautogui.hotkey("ctrl", "alt", "shift", "a")
# 순서대로 누르고 역순으로 떼는 명령
# pyautogui.hotkey("ctrl", "a")

import pyperclip
pyperclip.copy("나도코딩") # 한글 글자를 클립보드에 저장
pyautogui.hotkey("ctrl", "v") # 클립보드에 있는 내용을 붙여넣기 

def my_write(text):
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl","v")

my_write("나도코딩")

# 자동화 프로그램 종료
# win : ctrl + alt + del 
# mac : cmd + shift + option + q
