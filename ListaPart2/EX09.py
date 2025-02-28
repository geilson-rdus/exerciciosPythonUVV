# Escrever um algoritmo em Python que determine a conversão entre as moedas: Real, Dólar e Libra,
# de uma determinada quantidade em espécie e moeda informadas pelo usuário, sabendo que:
# R$ 4.08 = US$ 1.12 = £ 1.0 (Ver no Google a Cotação do "dia")

try:
    moeda = input('Escreva R para reais, L para Libras ou D para dólar: ')
    valorOriginal = float(input('Informe o valor na moeda escolhida: '))
    
    if(valoOriginal < 0):
        print('ERRO: Entrada inválida! Digite um número válido para o valor.')
    else:
        if moeda.lower() == 'r':
            conversao1 = valorOriginal / 4.08  # Converte para dólares
            conversao2 = conversao1 * 1.12  # Converte para libras
            print(f'O valor informado em reais foi R${valorOriginal:.2f}, que em dólares é ${conversao1:.2f} e em libras é £{conversao2:.2f}')
        
        elif moeda.lower() == 'l':
            conversao3 = valorOriginal * 4.08  # Converte para reais
            conversao4 = valorOriginal * 1.12  # Converte para dólares
            print(f'O valor informado em libras foi £{valorOriginal:.2f}, que em dólares é ${conversao4:.2f} e em reais é R${conversao3:.2f}')
        
        elif moeda.lower() == 'd':
            conversao5 = valorOriginal * 4.08 / 1.12  # Converte para reais
            conversao6 = valorOriginal / 1.12  # Converte para libras
            print(f'O valor informado em dólares foi ${valorOriginal:.2f}, que em reais é R${conversao5:.2f} e em libras é £{conversao6:.2f}')
        else:
            print('ERRO: Moeda inválida!')
except Exception as ERRO_EXCECAO:
  print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')
