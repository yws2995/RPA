import pyautogui
# 이미지를 찾아서 중간을 클릭  
# file_menu = pyautogui.locateOnScreen("file_menu.png")

# print(file_menu)
# pyautogui.click(file_menu)
# pyautogui.moveTo(file_menu) 이렇게 하는 방법도 있음

# screen = pyautogui.locateOnScreen("screenshot.png")
# print(screen)

# for i in pyautogui.locateAllOnScreen("checkbox.png"): #화면상 모든 체크박스 이미지를 클릭하도록 
#     print(i)
#     pyautogui.clicl(i)

# trash_icon = pyautogui.locateOnScreen("trash_icon.png")
# pyautogui.moveTo(trash_icon)

# 속도 개선을 위한 방법
# 1. GrayScale 흑백으로 바꿔서 30% 정도 속도를 개선
# trash_icon = pyautogui.locateOnScreen("trash_icon.png", grayscale = True)
# pyautogui.moveTo(trash_icon)

# 2. 범위 지정

# trash_icon = pyautogui.locateOnScreen("trash_icon.png", region = (x,y,width,height))
# pyautogui.moveTo(trash_icon)

# 3. 정확도 조정
# run_btn = pyautogui.locateOnScreen("run_btn.png", confidence = 0.9)
# pyautogui.moveTo(run_btn)

# 자동화 대상이 바로 보이지 않는 경우
# 1. 계속 기다리기
# file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
# # if file_menu_notepad:
# # pyautogui.click(file_menu_notepad)
# # else:
# #     print("발견 실패")
# while file_menu_notepad is None:
#     file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
#     print("발견 실패")

# pyautogui.clocl(file_menu_notepad)


# 2. 일정 시간동안 기다리기(TimeOut)
import time
import sys

# timeout = 10 # 10초 대기
# start = time.time() # 시작 시간 설정
# file_menu_notepad = None
# while file_menu_notepad is None:
#     file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
#     end = time.time() # 종료 시간 설정
#     if end - start  > timeout: # 지정한 10초를 초과하면
#         print("시간 종료")
#         sys.exit()
# pyautogui.click(file_menu_notepad)
def find_target(img_file, timeout = 30):
    start = time.time()
    target = None
    while target is None:
        target = pyautogui.locateOnScreen(img_file)
        end = time.time()
        if end - start > timeout:
            break
    return target

def my_click(img_file, timeout = 30):
    target = find_target(img_file, timeout)
    if target:
        pyautogui.click(target)
    else:
        print(f"[TImeout {timeout}s Target not found({img_file}). Terminate program.")
        sys.exit()

my_click("file_menu_notepad.png", 10)