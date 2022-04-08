import pyautogui

# fw = pyautogui.getActiveWindow() # 현재 활성화된 창 정보를 가져온다 (현재는 VSCode)
# print(fw.title) # 차의 제목 정보
# print(fw.size) # 창의 크기 정보
# print(fw.left, fw.top, fw.right, fw.bottom) # 창의 좌표정보

# pyautogui.click(fw.left + 25, fw.top + 20)

# for w in pyautogui.getAllWindows():
#     print(w) # 모든 창 가져오기

w = pyautogui.getWindowsWithTitle("제목 없음")[0]
print(w)
if w.isActive == False:
    w.activate() # 활성회 ( 맨 앞으로 화면 가져오기 )

if w.isMaximized == False: # 현재 최대화가 되지 않았다면
    w.maximize() # 최대화

# if w.isMinimized == False: # 현재 최소화가 되지 않았다면
#     w.minimize()
pyautogui.sleep(1)
w.restore() # 화면 원복

w.close() # 윈도우 닫기 