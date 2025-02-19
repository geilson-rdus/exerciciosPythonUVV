# Tendo como dado de entrada a altura (h) e o sexo de uma pessoa, construa um algoritmo que calcule seu peso (Massa: Quilogramas) ideal

try: 
    altura = float(input('Informe sua altura em metros: '))
    sexo = input('Informe seu sexo: ')
    if(altura <= 0):
        print('ERRO: Dados de Entrada')
    else:
        if(sexo.lower() == 'homem'):
            pesoIdeal = (72.7 * altura) - 58
            print(f'Seu peso ideal é {pesoIdeal: .2f} Kg')
        elif(sexo.lower() == 'mulher'):
            pesoIdeal = (62.1 * altura) - 44.7
            print(f'Seu peso ideal é {pesoIdeal: .2f} Kg')
        else:
            print('ERRO: Dados de Entrada')
except:
    print('ERRO: Dados de Entrada')
