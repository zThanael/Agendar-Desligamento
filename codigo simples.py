
import os

horas = int(input('Deseja desligar o computador após quantas horas: '))
segundos = horas * 3600
os.system(f'shutdown -s -t {segundos}')
cancelar = int(input('Caso deseje cancelar o agentamento digite 0: '))
if cancelar == 0:
    os.system('shutdown -a')


