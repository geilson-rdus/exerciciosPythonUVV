# Escrever um algoritmo em Python que exiba o público total (inteiro) de um jogo de futebol e forneça a arrecadação (R$: real) do jogo

try: 
    publicoTotal = int(input('Público total presente: '))
    criancasMenos10 = int(input('Quantidade de crianças menores de 11 anos: '))
    criancasEntre11E17 = int(input('Quantidade de crianças entre 11 e 17 anos: '))
    adultosDoadores = int(input('Maiores de 18 anos que doaram 1 kg de alimento: '))
    valorIngresso = float(input('Valor inteiro do ingresso em reais: '))
    
    publicoMeia = criancasMenos10 + criancasEntre11E17 + adultosDoadores
    
    if(publicoTotal < 0 or criancasMenos10 < 0 or criancasEntre11E17 < 0 or adultosDoadores < 0 or valorIngresso <= 0):
        print('ERRO: Dados de Entrada')
    elif(publicoMeia > publicoTotal):
        print('ERRO: Dados de Entrada')
    else:
        publicoPagaInteira = publicoTotal - publicoMeia
        arrecadacao = (criancasEntre11E17 * (valorIngresso/2)) + (adultosDoadores * (valorIngresso/2)) + (publicoPagaInteira * valorIngresso)
        print(f'O público total foi {publicoTotal} e o a arrecadação foi R${arrecadacao: .2f}')
except:
    print('ERRO: Dados de Entrada')
