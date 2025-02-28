import math
try: 
    raio = float(input('Insira um valor maior que 0: '))
    if(raio <= 0):
        print('ERRO: Você inseriu um valor negativo ou zero')
    else:
        volumeEsfera = 4 * math.pi * (raio ** 3) / 3
        areaEsfera = 4 * math.pi * (raio ** 2)
        print(f'O volume da esfera é{volumeEsfera: .2f} m^3 e a área é{areaEsfera: .2f} m^2')
except Exception as ERRO_EXCECAO:
    print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')
