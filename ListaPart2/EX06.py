# Faça um algoritmo que leia um número positivo e exiba se seu quadrado é ímpar e múltiplo de 11.

try: 
    numero = int(input('Informe um número inteiro e positivo'))
    
    if(numero <= 0):
        print('ERRO: Dados de Entrada')
    else:
        quadrado = numero ** 2
        if(quadrado % 2 != 0 and quadrado % 11 == 0):
            print(f'O número digitado foi {numero}. Seu quadrado é {quadrado},  que é ímpar e múltiplo de 11')
        else:
            print(f'O número digitado foi {numero}. Seu quadrado é {quadrado},  que não é ímpar ou não é múltiplo de 11')
except Exception as ERRO_EXCECAO:
  print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')
