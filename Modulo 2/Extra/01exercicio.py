# 1. Crie um programa que use um comando com o Pyautogui para abrir a calculadora do Windows e faça um calculo de 8 + 2 e apresente o resultado.
# Observação: Utilizando o Win + R
# para abrir o Executar, digitar "calc"
# e pressionar Enter.

import pyautogui
import time

pyautogui.hotkey('win', 'r')
time.sleep(1)
pyautogui.write('calc')
pyautogui.press('enter')
time.sleep(2)

pyautogui.write('8 + 2')
pyautogui.press('enter')
time.sleep(2)

