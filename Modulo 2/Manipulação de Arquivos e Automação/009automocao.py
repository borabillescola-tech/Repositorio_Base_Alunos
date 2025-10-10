# Desenhar um objeto
# Após a execução do código abra um bloco de notas para o desenho ser criado

import pyautogui
import time

pyautogui.press('win')
time.sleep(1)
pyautogui.write('bloco de notas')
pyautogui.press('enter')
time.sleep(1)

arvore = [
    "    *    ",
   "   ***   ",
   "  *****  ",
   " ******* ",
   "*********"
]

for linha in arvore:
    pyautogui.write(linha)
    pyautogui.press('enter')
pyautogui.write("   |||   ")
pyautogui.press('enter')

