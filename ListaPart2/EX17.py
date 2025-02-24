# Escrever um algoritmo que leia três (3) valores reais e positivos: A, B e C e verifique se formam um
# triângulo. Além disso; se formarem um triângulo dizer qual tipo, a saber:

try:
    A = float(input('Informe o primeiro número real: '))
    B = float(input('Informe o segundo número real: '))
    C = float(input('Informe o terceiro número real: '))
    if(A<0 or B<0 or C<0):
        print('ERRO: Você informou números menores que zero')
    else:
        if(A < B+C and B < A+C and C < A+B):
            if(A==B and B==C):
                print(f'Os números ({A:.2f}),({B:.2f}) e ({C:.2f}) formam um triângulo equilátero')
            elif((A==B or B==C or A==C) and (A!=B or B!=C or A!=C)):
                print(f'Os números ({A:.2f}),({B:.2f}) e ({C:.2f}) formam um triângulo isósceles')
            else:
                print(f'Os números ({A:.2f}),({B:.2f}) e ({C:.2f}) formam um triângulo escaleno')
        else:
            print(f'Os números ({A:.2f}),({B:.2f}) e ({C:.2f}) não formam um triângulo')
except Exception as ERRO_EXCLUSAO:
    print(f'ERRO: {ERRO_EXCLUSAO}')
