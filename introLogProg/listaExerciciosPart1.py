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

# EXERCÍCIO 1 h) Calcular e exibir a quantidade de tinta (em latas) e o custo (em reais) para pintar um tanque cilíndrico de base circular de Raio (R) e altura (H) em metros,

try: 
    alturaCilindro = float(input('Informe a altura do tanque cilíndrico em metros: '))
    raioCilindro = float(input('Informe o raio do tanque cilíndric em metros: '))
    if(alturaCilindro <= 0 or raioCilindro <= 0):
        print('ERRO: Dados de Entrada')
    else:
        areaBaseCilindro = 3.14 * (raioCilindro ** 2)
        comprimentoBaseCilindro = 2 * 3.14 * raioCilindro
        areaCorpoCilindro = comprimentoBaseCilindro * alturaCilindro
        areaTotalCilindro = (2 * areaBaseCilindro) + areaCorpoCilindro
        
        qtdLatasTinta = round(areaTotalCilindro / 15 , 0)
        preco = qtdLatasTinta * 50
        
        print(f'Quantidade de latas: {qtdLatasTinta: .0f}')
        print(f'Preço em reais: R$ {preco: .2f}')
except:
    print('ERRO: Dados de Entrada')

# EXERCÍCIO 1 i) Calcular e exibir a distância entre dois pontos quaisquer do plano, P(x1, y1) e Q(x2, y2), sabendo que a fórmula da distância é d = √(x2 – x1) 2 + (y2 – y1) 2, sendo os pontos P(x1, y1) e Q(x2, y2) como dados de entrada.

try: 
    pontoAX = float(input('Primeiro elemento do par ordenado do ponto A: '))
    pontoAY = float(input('Segundo elemento do par ordenado do ponto A: '))
    pontoBX = float(input('Primeiro elemento do par ordenado do ponto B: '))
    pontoBY = float(input('Segundo elemento do par ordenado do ponto B: '))
    
    distancia = (((pontoBX - pontoAX) ** 2) + ((pontoBY - pontoAY) ** 2)) ** (1/2)
    
    print(f'A distância entre os pontos é {distancia: .2f}')
    
except:
    print('ERRO: Dados de Entrada')

# EXERCÍCIO 1 j) Calcular e exibir o tempo (em horas) de autonomia de uma caixa d’água de um restaurante que consome 1350 litros por hora em média. O tanque do restaurante é cilíndrico de base circular de Raio (R) e de altura (H) em metros. Sabendo que 1 m3 = 1000 Litros.

try: 
    alturaCilindro = float(input('Informe a altura do tanque cilíndrico em metros: '))
    raioCilindro = float(input('Informe o raio do tanque cilíndric em metros: '))
    if(alturaCilindro <= 0 or raioCilindro <= 0):
        print('ERRO: Dados de Entrada')
    else:
        volumeCilindro = 3.14 * (raioCilindro ** 2) * alturaCilindro * 1000
        autonomia = round(volumeCilindro / 1350,0)
        
        print(f'A autonomia do tanque é de aproximadamente {autonomia: .0f} horas')
except:
    print('ERRO: Dados de Entrada')

# EXERCÍCIO 1 k) Faça um programa que peça o tamanho de um arquivo para download (em Megabytes) e a velocidade de um link de Internet (em Megabytes / Segundo), calcule e informe o tempo: Minutos + Segundos aproximado de download do arquivo usando este link.

try: 
    tamanhoArquivo = float(input('Tamanho do arquivo em megabytes: '))
    velocidadeDownload = float(input('Velocidade de download em megabytes por segundo: '))
    if(tamanhoArquivo <= 0 or velocidadeDownload <= 0):
        print('ERRO: Dados de Entrada')
    else:
        tempoDownload = tamanhoArquivo / velocidadeDownload
        
        minutos, segundos = divmod(tempoDownload, 60)
        
        print(f'O tempo de dowload é: {minutos: .0f}minutos e {segundos: .0f}segundos')
except:
    print('ERRO: Dados de Entrada')

# EXERCÍCIO 1 l)Calcular e exibir a distância máxima (em Quilômetros) de autonomia de um carro que possui um tanque de combustível cúbico de lado (L) em metros e Altura (h) de preenchimento do tanque. Sabendo que seu consumo é em média 10 km/litro. Sabendo que 1 m3 = 1000 Litros.

try: 
    ladoCubo = float(input('Lado do tanque cúbico em metros: '))
    if(ladoCubo <= 0):
        print('ERRO: Dados de Entrada')
    else:
        volumeTanque = (ladoCubo ** 3) * 1000
        
        autonomiaCarro = volumeTanque / 10
        
        print(f'A distância distância máxima (em Quilômetros) de autonomia do carro é {autonomiaCarro: .2f} km')
except:
    print('ERRO: Dados de Entrada')
