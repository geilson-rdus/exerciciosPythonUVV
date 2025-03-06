# Escrever um algoritmo em Python que exiba o público total (inteiro) de um jogo de futebol e forneça a arrecadação (R$: real) do jogo

try: 
    adultosInteira = int(input('Maiores de 18 que pagaram inteira: '))
    criancasMenos10 = int(input('Quantidade de crianças menores de 11 anos: '))
    criancasEntre11E17 = int(input('Quantidade de crianças entre 11 e 17 anos: '))
    adultosDoadores = int(input('Maiores de 18 anos que doaram 1 kg de alimento: '))
    valorIngresso = float(input('Valor inteiro do ingresso em reais: '))
    
    publicoMeia = criancasEntre11E17 + adultosDoadores
    publicoTotal = publicoMeia + adultosInteira + criancasMenos10
    
    if(adultosInteira < 0 or criancasMenos10 < 0 or criancasEntre11E17 < 0 or adultosDoadores < 0 or valorIngresso <= 0):
        print('ERRO: Informou valores negativos')
    else:
        arrecadacao = (publicoMeia * (valorIngresso/2)) + (adultosInteira * valorIngresso)
        print(f'O público total foi de {publicoTotal} pessoas e a arrecadação foi R${arrecadacao: .2f}')
except Exception as ERRO_EXCECAO:
  print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')
