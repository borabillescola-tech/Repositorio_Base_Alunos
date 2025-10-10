import pyautogui
import webbrowser
import time

# Passo 1: Abrir o youtube com um vídeo específico
url = 'https://youtu.be/_UsKlaZmLZo?si=sdcB22za3GGL9wWO'
webbrowser.open(url)

# Passo 2: Aguardar o carregamento da página
time.sleep(5) # Ajustar de acordo com a velocidade da internet utilizada

# Passo 3: Garantir que o vídeo comece (aperte o espaço para o 'play')
pyautogui.press('space') # toca ou pausa o vídeo



