#calcula o preco com e sem desconto de um produto

preco = float(input('Informe o preço do produto em reais: '))
quantidadeProduto = int(input('Informe a quantidade do produto: '))
desconto = float(input('Informe o desconto total: '))

valorTotal = preco * quantidadeProduto

print(f'O total a ser pago sem desconto: {valorTotal:.2f}')
print(f'O total a ser pago com desconto: {valorTotal - (valorTotal * (desconto/100)):.2f}')
