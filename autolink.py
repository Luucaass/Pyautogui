!pip install pyautogui

import pyautogui  #import library pyautogui/importa a biblioteca pyautogui
import time       #import library time/importa a biblioteca time


#here will press ctrl+t on your keyboard/aqui ira pressionar ctrl+t no seu teclado
pyautogui.hotkey("ctrl", "t")
#here wait 2 seconds for the page load/aqui espera 2 segundos para a pagina carregar
time.sleep(2)
#here will copy the link(you can use another link here)/aqui ira copiar o link(voce pode usar outro link aqui)
pyperclip.copy("https://www.youtube.com/watch?v=dQw4w9WgXcQ") 
#here gonna press ctrl+v for paste the link/aqui vai pressionar ctrl+v para colar o link
pyautogui.hotkey("ctrl", "v")
#here will press enter on your keyboard and run the link/aqui ira pressionar enter no seu teclado e iniciar o link
pyautogui.hotkey("enter") 
