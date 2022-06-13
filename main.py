import PySimpleGUI as sg
from time import sleep
import webbrowser
import sys
from colorama import Fore

sg.theme('DarkAmber')

bad_column = [
    [
        sg.Text('Licensed under Creative Commons'),
    ],
]

layout = [  
            [sg.Column(bad_column)],
            [sg.Text('Token Cracker')],
            [sg.Text('Enter User ID'), sg.InputText()],
            [sg.Button('OK'), sg.Button('Cancel')] ]

words = Fore.BLUE + "HOWARD\n"
for char in words:
    sleep(0.055)
    sys.stdout.write(char)
    sys.stdout.flush()

window = sg.Window('Howard', layout, size=(400,400))
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': 
        break
    sleep(1)
    print("Token: OTc5ODkzNjQzNzg5ODg1NDYw.GoPwqO.pfYp6nFHgkbiWDQFwuaJC7NnY1VziSUrertj4g")
window.close()

sleep(4)
webbrowser.open('https://i.kym-cdn.com/photos/images/newsfeed/000/909/987/14a.jpg')


            
            
            



