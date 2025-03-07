# Escrever um algoritmo em Python que leia o Preço de uma mercadoria e exiba o preço na tela
# reajustado de 3%. O usuário escolherá a Opção: “Acréscimo” ou “Desconto” para o reajuste de 3 %.
# Faça agora o mesmo exercício, entretanto; lendo o reajuste (em %) do usuário.

try: 
    preco = float(input('Informe o preço da mercadoria em reais: '))
    reajuste = float(input('Informe o reajuste em porcentagem: '))
    tipoReajuste = input('Desconto(d) ou Acréscimo(a): ')
    
    if(preco < 0 or reajuste < 0 or reajuste > 100):
        print('ERRO: Valores de preço ou reajuste inválidos')
    else:
        if(tipoReajuste.lower() == 'd'):
            precoAjuste = preco * (1 - (reajuste / 100))
            print(f'O preço informado foi R${preco: .2f}, com um desconto de {reajuste:.2f}%, resultou num preço de R${precoAjuste: .2f}')
        elif(tipoReajuste.lower() == 'a'):
            precoAjuste = preco * (1 + (reajuste / 100))
            print(f'O preço informado foi R${preco: .2f}, com um acréscimo de {reajuste:.2f}%, resultou num preço de R${precoAjuste: .2f}')
        else:
            print('ERRO: Inseriu um valor não correspondente com as opções')
except Exception as ERRO_EXCECAO:
  print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')
