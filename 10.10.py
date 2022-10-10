import PySimpleGUI as sg

sg.theme('DarkAmber')
  
layout = [
    [sg.Text('Ievadi datus')],
    [sg.Text('Vards', size =(27, 1)), sg.InputText()],
    [sg.Text('veltijums', size =(27, 1)), sg.InputText()],
    [sg.Submit(), sg.Cancel()], [sg.Button('Exit')]
]  

window= sg.Window('Dati ievade', layout)

while True:
    event, values = window.read()
    if event is ('Exit'):
        break


window.close()
