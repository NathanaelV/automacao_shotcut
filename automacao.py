import pyautogui
from time import sleep

# Mouseinfo para conseguir as coordenadas do seu mouse
# - abra o terminal python com: python3
# - importe o mouseinfo com: from mouseinfo import mouseInfo
# - digite: mouseInfo() para executar o programa e coletar as informações do mouse

# 1 - Clicar e digitar meu usuário
pyautogui.click(4335,421,duration=0.5, button='left')

# Rodar a tela para baixo.
pyautogui.scroll(-10)
# 2 - Clicar e digitar minha senha
