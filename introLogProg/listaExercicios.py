# EXERCÍCIO 1 a) Calcular e exibir a hipotenusa (A) de um triângulo retângulo de catetos (B) e (C), sabendo que:

try: 
    catetoA = float(input('Informe o cateto A: '))
    catetoB = float(input('Informe o cateto B: '))
    if(catetoA <= 0 or catetoB <= 0):
        print('ERRO: Dados de Entrada')
    else:
        hipotenusa = ((catetoA**2) + (catetoB**2))**(1/2)
        print(f'Hipotenusa: {hipotenusa: .2f}')
except:
    print('ERRO: Dados de Entrada')

# EXERCÍCIO 1 b) Calcular e exibir a área de um quadrado de lado (L). Área = L2

try: 
    ladoQ = float(input('Informe o lado do quadrado: '))
    if(lado <= 0):
        print('ERRO: Dados de Entrada')
    else:
        areaQ = ladoQ**2
        print(f'Área do Quadrado: {area: .2f}')
except:
    print('ERRO: Dados de Entrada')

# EXERCÍCIO 1 c) Calcular e exibir a área de um retângulo de lado (L) e altura (H). Área = L * H.

try: 
    ladoR = float(input('Informe o lado do retângulo: '))
    alturaR = float(input('Informe a altura do retângulo: '))
    if(ladoR <= 0 or alturaR <= 0):
        print('ERRO: Dados de Entrada')
    else:
        areaR = ladoR * alturaR
        print(f'Área do Retângulo: {areaR: .2f}')
except:
    print('ERRO: Dados de Entrada')

# EXERCÍCIO 1 d) Calcular e exibir a área e o comprimento de um círculo de Raio (R), sabendo que, Área = π * R2 e Comprimento = 2 * π * R.

try: 
    raio = float(input('Informe o raio do círculo: '))
    if(raio <= 0):
        print('ERRO: Dados de Entrada')
    else:
        areaC = 3.14 * (raio ** 2)
        comprimentoC = 2 * 3.14 * raio
        print(f'Área do Círculo: {areaC: .2f}')
        print(f'Comprimento do Círculo: {comprimentoC: .2f}')
except:
    print('ERRO: Dados de Entrada')

# EXERCÍCIO 1 e) Calcular e exibir o IMC (Índice de Massa Corpórea) de uma pessoa de altura (H) em metros e massa (M) em quilogramas, sabendo que IMC = M / H2

try: 
    altura = float(input('Informe sua altura em metros: '))
    massa = float(input('Informe sua massa em quilogramas: '))
    if(altura <= 0 or massa <= 0):
        print('ERRO: Dados de Entrada')
    else:
        IMC = massa/(altura**2)
        print(f'Seu IMC: {IMC: .2f}')
except:
    print('ERRO: Dados de Entrada')

# EXERCÍCIO 1 f) Calcular e exibir o volume em litros de uma esfera de Raio (R), sabendo que o usuário deve informar o Raio (R) em metros. Sabe-se que: VolumeEsfera = 4 3 ⁄ * π * R3 e que 1 Litro é igual a 10-3 m3.

try: 
    raio = float(input('Informe o raio em metros: '))
    if(raio <= 0):
        print('ERRO: Dados de Entrada')
    else:
        volume = (4 * 3.14 * (raio ** 3))/3
        volume *= 1000
        print(f'O volume da esfera em litros: {volume: .2f}L')
except:
    print('ERRO: Dados de Entrada')

# EXERCÍCIO 1 g) Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato. Com isso, exiba na tela:

try: 
    valorHora = float(input('Informe o seu salário por hora trabalhada em reais: '))
    horasTrabalhadas = float(input('Informe a quantidade de horas trabalhadas: '))
    if(valorHora <= 0 or horasTrabalhadas <= 0):
        print('ERRO: Dados de Entrada')
    else:
        salario = valorHora * horasTrabalhadas
        inss = salario * 0.08
        sindicato = salario * 0.05
        liquido = salario - inss - sindicato - (salario*0.11)
        
        print(f'Salário bruto: R${salario: .2f}')
        print(f'Quanto pagou ao INSS: R${inss: .2f}')
        print(f'Quanto pagou ao sindicato: R${sindicato: .2f}')
        print(f'Salário líquido: R${liquido: .2f}')
except:
    print('ERRO: Dados de Entrada')
