# Escrever um algoritmo que leia três (3) valores reais quaisquer e distintos (teste e avise ao usuário
# se os valores informados forem iguais) e exiba na saída a média dos dois maiores números lidos.

try:
    n1 = float(input('Informe o primeiro número real: '))
    n2 = float(input('Informe o segundo número real: '))
    n3 = float(input('Informe o terceiro número real: '))
    if(n1==n2 or n1==n3 or n2==n3):
        print('ERRO: Você informou números iguais')
    else:
        soma = 0
        if(n1>n2 or n1>n3):
            soma += n1
        if(n2>n3 or n2>n1):
            soma += n2
        if(n3>n1 or n3>n2):
            soma += n3
        media = soma/2
        print(f'A média entre os dois maiores números é {media:.2f}')
except Exception as ERRO_EXCLUSAO:
    print(f'ERRO: {ERRO_EXCLUSAO}')
