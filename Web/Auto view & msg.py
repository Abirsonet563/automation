#Msg (FB, Insta, Twitter, GitHub)
import pyautogui
import time
while True:
    time.sleep(0.5)
    pyautogui.typewrite('“Hope all your birthday wishes come true!” Happy_Birth_Day Saif :)"')
    pyautogui.press('enter')

#Web Auto View
import time
import webbrowser

count = 0
urls = ['https://www.youtube.com/watch?v=Dq7yHiCjKrA']

while count < 100:
    for url in urls:
        webbrowser.open(url, new=0)
        time.sleep(10)
        Cout = count +1
else:
    pass
