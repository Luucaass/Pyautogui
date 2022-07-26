import pyautogui
import pyperclip
import time

#Hello, my name is lucas, im student of Computer Science. In this code you will see all my networks.
#Ola, meu nome é lucas,sou estudante de ciencia da computação. Neste codigo voce vai ver todas minhas redes de contato.

pyautogui.hotkey("ctrl", "t")
time.sleep(2)

#My GitHub / Meu GitHub

pyperclip.copy("https://github.com/Luucaass")
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("enter")
time.sleep(7)
pyautogui.hotkey("ctrl", "w")

pyautogui.hotkey("ctrl", "t")
time.sleep(2)

#My LinkedIn / Meu LinkedIn

pyperclip.copy("https://www.linkedin.com/in/lucas-gabriel-65825b229/")
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("enter")
time.sleep(7)
pyautogui.hotkey("ctrl", "w")
