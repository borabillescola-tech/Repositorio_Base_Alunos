# Crie uma automoção que faça o mouse se mover na forma de um quadrado
# Importamos a biblioteca pyautogui
import pyautogui 

for i in range(10): # Repetimos 10 vezes
# A função .moveTo é uma função para movimento do mouse
# pyautogui .moveTo (x,y , duration=tempo em segundos)
    pyautogui.moveTo(100 + 10 * i, 100 + 10 * i, duration=0.5) # Move o mouse para a posição (100,100) em 0.5 segundos
    pyautogui.moveTo(200 + 10 * i, 100 + 10 * i, duration=0.5) # Move o mouse para a posição (200,100) em 0.5 segundos
    pyautogui.moveTo(200 + 10 * i, 200 + 10 * i, duration=0.5) # Move o mouse para a posição (200,200) em 0.5 segundos
    pyautogui.moveTo(100 + 10 * i, 200 + 10 * i, duration=0.5) # Move o mouse para a posição (100,200) em 0.5 segundos

