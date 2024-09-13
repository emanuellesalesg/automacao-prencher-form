import pyautogui
import time

pyautogui.PAUSE = 0.3
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.click(x=687, y=436)

time.sleep(1)

pyautogui.write("https://www.hashtagtreinamentos.com/")
pyautogui.press("enter")
time.sleep(3)


posicao_cursopython = pyautogui.locateCenterOnScreen("curso_python.png")
pyautogui.click(posicao_cursopython)

pyautogui.click(x=590, y=625)
pyautogui.write("Emanuelle")


pyautogui.press("tab")
pyautogui.write("email@gmail.com")


pyautogui.press("tab")
pyautogui.write("(98)76765-5540")

