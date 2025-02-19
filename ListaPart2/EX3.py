# Faça um algoritmo em Python que leia o tempo (segundos) de permanência de um aluno no Laboratório de Programação: UVV e exiba na tela seu tempo de permanência: Horas + Minutos + Segundos. Exemplo: Tempo: 10000 Segundos = 2 Hora(s) + 46 Minuto(s) + 40 Segundo(s).

try: 
    tempo = float(input('Insira o tempo em segundos: '))
    if(tempo < 0):
        print('ERRO: Dados de Entrada')
    else:
        horas, resto = divmod(tempo,3600)
        minutos, segundos = divmod(resto,60)
        print(f'Tempo: {horas: .0f} hora(s) {minutos: .0f} minuto(s) {segundos: .0f} segundo(s)')
except:
    print('ERRO: Dados de Entrada')
