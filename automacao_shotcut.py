import pyautogui
import pyperclip
from time import sleep

arr =  ["Hotmart Club - Aula Magna - 02_02_2022 - Google Chrome 2023-05-03 12-58-22.mp4", 'Seminário Online Meganet - Google Chrome 2022-11-26 15-16-41.mp4']


pyautogui.click(618,55,duration=0.1, button='left')

for text in arr:
  # pyautogui.hotkey('ctrl', 'o')

  pyautogui.sleep(2)

  # text = 'Hotmart Club - 7 - CORAGEM_ O principal recurso para conquistar a VIDA ÉPICA! - Google Chrome 2023-04-15 18-02-32.mp4'
  # print(text)
  pyperclip.copy(text)
  pyautogui.sleep(0.5)
  pyautogui.hotkey('ctrl', 'v')
  pyautogui.sleep(2) # Remover

  pyautogui.press('enter')

  pyautogui.sleep(2)

  # pyautogui.hotkey('ctrl', 'e')

  # pyautogui.sleep(2)

  pyperclip.copy(text[0:-4])
  pyautogui.hotkey('ctrl', 'v')
  pyautogui.sleep(2) # Remover

  pyautogui.press('enter')

  pyautogui.sleep(2)

  # pyautogui.click(1114,552,duration=0.1, button='left')

  # pyautogui.sleep(2)

