# Automoção de login fictício
# Ideias: Preencher automaticamente um formulário
# (HTML local ou simulado, via bloco de notas).

import pyautogui, time 
time.sleep(3)
pyautogui.write('Caio Jardim', interval=0.1)
pyautogui.press('tab')
pyautogui.write('senha123', interval=0.1)
pyautogui.press('enter')
