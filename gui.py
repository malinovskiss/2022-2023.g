import PySimpleGUI as sg

sg.theme('DarkAmber')

layout = [[sg.Text('Nospied!'),sg.Button('Šķēres')],
[sg.Text('',key='-LEMUMS-')],
[sg.Button('Neizvērt')],
[sg.Button('Aizvērt')]]

window = sg.window('Spēle',layout)

while True:
    event, values = window.read()
    if event == 'Šķēres':
        window['-LEMUMS-'].update('Izvēle: šķēres')
    if event == 'Neaizvērt':
        vards = values[0]
    if event == 'Aizvērt':
        break

window.close()