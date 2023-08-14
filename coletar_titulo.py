import pyautogui
from time import sleep

pyautogui.click(305,119,duration=0.5, button='left')

str = '/home/nathanael/Videos/2022-10-25 16-18-27.mkv /home/nathanael/Videos/2022-10-27 09-42-03.mkv /home/nathanael/Videos/Conversa com o Maurício 26.10.22.mkv /home/nathanael/Videos/Login no myHonda.mkv /home/nathanael/Videos/Mudar as lojas de custler.mkv'

arr = str.split('/home/nathanael/Videos/')

# Ruby
# arr.each(&:strip)

arr = ["Hotmart Club - Gestão do Tempo com Tiago Correa - 01_02_2023 - Google Chrome 2023-05-06 18-56-28.mp4 ", "Hotmart Club - Live 05_07_22 - Perguntas e Respostas - Google Chrome 2023-05-04 22-19-38.mp4"]



'/media/nathanael/HD - Ana/Curso gravado/original/Hotmart Club - Gestão do Tempo com Tiago Correa - 01_02_2023 - Google Chrome 2023-05-06 18-56-28.mp4 /media/nathanael/HD - Ana/Curso gravado/original/Hotmart Club - Live 05_07_22 - Perguntas e Respostas - Google Chrome 2023-05-04 22-19-38.mp4'