import pyautogui
# 스크린 샷
# img = pyautogui.screenshot()
# img.save("screenshot.png") # 파일로 저장

# pyautogui.mouseInfo()
# 1108,92 204,204,204 #CCCCCC

pixel = pyautogui.pixel(1108,92)
print(pixel)

print(pyautogui.pixelMatchesColor(1108,92, pixel))