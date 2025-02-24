# Escrever um algoritmo que leia cinco (5) valores inteiros Positivos e distintos (teste e avise ao
# usuário se os valores informados forem iguais) e exiba na saída a média dos números PARES e a
# média dos números ÍMPARES lidos do usuário.

try:
    n1 = int(input('Informe o primeiro número inteiro positivo: '))
    n2 = int(input('Informe o segundo número inteiro positivo: '))
    n3 = int(input('Informe o terceiro número inteiro positivo: '))
    n4 = int(input('Informe o quarto número inteiro positivo: '))
    n5 = int(input('Informe o quinto número inteiro positivo: '))
    if(n1==n2 or n1==n3 or n1==n4 or n1==n5 or n2==n3 or n2==n4 or n2==n5 or n3==n4 or n3==n5 or n4==n5):
        print('ERRO: Você informou números iguais')
    else:
        somaPares = 0
        somaImpares = 0
        qtdPares = 0
        qtdImpares = 0
        if(n1%2==0):
            somaPares += n1
            qtdPares += 1
        else:
            somaImpares += n1
            qtdImpares += 1
        if(n2%2==0):
            somaPares += n2
            qtdPares += 1
        else:
            somaImpares += n2
            qtdImpares += 1
        if(n3%2==0):
            somaPares += n3
            qtdPares += 1
        else:
            somaImpares += n3
            qtdImpares += 1
        if(n4%2==0):
            somaPares += n4
            qtdPares += 1
        else:
            somaImpares += n4
            qtdImpares += 1
        if(n5%2==0):
            somaPares += n5
            qtdPares += 1
        else:
            somaImpares += n5
            qtdImpares += 1
        
        mediaPares = 0
        mediaImpares = 0
        
        if(qtdPares>0):
            mediaPares = somaPares / qtdPares
        if(qtdImpares>0):
            mediaImpares = somaImpares / qtdImpares
        
        print(f'A média dos pares é {mediaPares:.2f} e a média dos ímpares é {mediaImpares:.2f}')
except Exception as ERRO_EXCLUSAO:
    print(f'ERRO: {ERRO_EXCLUSAO}')
