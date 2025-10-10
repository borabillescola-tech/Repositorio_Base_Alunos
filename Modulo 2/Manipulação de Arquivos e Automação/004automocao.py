# Crie uma automoção que escreva um texto automaticamente

import pyautogui
import time

# Observação: Abra um bloco de notas vazio
# Aguarde 5 segundos para abrir o bloco de notas
time.sleep(5)

# Escreve um texto automaticamente
pyautogui.write("Olá, isso é uma automação!", interval=0.1)