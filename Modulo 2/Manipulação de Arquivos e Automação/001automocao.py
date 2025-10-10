# 1. Instalar o pyautogui com o comando:
# pip install pyautogui

# Crie uma automoção que abra automaticamente um navegador
# Importamos a biblioteca para o script em uso
import pyautogui

# 'Press' é um comando que utilizamos para pressionar uma tecla
pyautogui.press('win') # Abre o menu iniciar do windows

# Sleep é um comando que utilizamos para deixar o código em espera por alguns segundos
pyautogui.sleep(1) # Espera 1 segundo

# 'Write' é um comando que utilizamos para escrever algo
pyautogui.write('chrome') # Escreve 'chrome' no menu iniciar

pyautogui.press('enter') # Pressiona a tecla 'enter' para abrir o chrome
