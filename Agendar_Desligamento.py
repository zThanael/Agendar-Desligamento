from PySimpleGUI import PySimpleGUI as sg
import os

def agendar(horas):
    horas = int(horas)
    segundos = (horas  *  60) * 60
    os.system(f'shutdown -s -t {segundos}')

#layout 
layout = [
    [sg.Text('Desligar o computador após quantas horas: '),sg.Input(key='horas',size=(10,0))],
    [sg.Button('Agendar'), sg.Button('Cancelar')]
]
#criar a janela
janela = sg.Window('Agendar Desligamento',layout=layout, finalize=True)

#ler os eventos
while True:
    event,values = janela.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Agendar':
        agendar(values['horas'])
        sg.popup(f"Computador será desligado em {values['horas']} horas")
    if event == 'Cancelar':
        os.system('shutdown -a')
        sg.popup('Foi cancelado o desligamento')
