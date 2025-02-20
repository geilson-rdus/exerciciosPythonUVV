# Escrever um algoritmo em Python que leia uma temperatura em Celsius (C) ou Fahrenheit (F) e faça a conversão entre as unidades.

try: 
    escala = input('Escreva C para Celsius ou F para Fahrenheit: ')
    valorOriginal = float(input('Informe o valor na escala escolhida: '))
    if(escala.lower() == 'c'):
        conversao = ((9 * valorOriginal) / 5) + 32
        print(f'O valor informado em celsius foi{valorOriginal: .2f} C, que em fahrenheit é: {conversao: .2f} F')
    elif(escala.lower() == 'f'):
        conversao = ((valorOriginal - 32) * 5) / 9
        print(f'O valor informado em fahrenheit foi{valorOriginal: .2f} F, que em celsius é: {conversao: .2f} C')
    else:
        print('ERRO: Dados de Entrada')
except:
    print('ERRO: Dados de Entrada')
