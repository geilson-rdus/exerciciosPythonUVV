#Escrever um algoritmo em Python que determine o volume e a área de uma esfera de raio r (∈ R+∗). Sendo que π = 3.14.

try: 
    raio = float(input('Insira um valor maior que 0: '))
    if(raio <= 0):
        print('ERRO: Dados de Entrada')
    else:
        volumeEsfera = 4 * 3.14 * (raio ** 3) / 3
        areaEsfera = 4 * 3.14 * (raio ** 2)
        print(f'O volume da esfera é{volumeEsfera: .2f} m^3 e a área é{areaEsfera: .2f} m^2')
except:
    print('ERRO: Dados de Entrada')
