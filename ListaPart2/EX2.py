# Escrever um algoritmo em Python que leia a Base (B > 0) e a Altura (H > 0) de um retângulo em centímetros e calcule e exiba na tela seu Perímetro (soma dos lados) em:

try: 
    base = float(input('Base do retângulo em centímetros: '))
    altura = float(input('Altura do retângulo em centímetros: '))
    if(base <= 0 or altura <= 0):
        print('ERRO: Dados de Entrada')
    else:
        perimetro = 2*base + 2*altura
        perimetroPolegada = perimetro/2.54
        perimetroJardas = perimetroPolegada*0.03
        print(f'O perímetro: {perimetro: .2f} cm, {perimetroPolegada: .2f} polegadas e {perimetroJardas: .2f} jardas')
except:
    print('ERRO: Dados de Entrada')
