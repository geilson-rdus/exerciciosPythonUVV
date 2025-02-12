'''
VERSÃO PLUS:
Refazer o algoritmo anterior, dando a opção para o usuário escolher a Proporção de combustível.
'''
larguraTanque = float(input('Qual a largura do tanque em metros? '))
alturaTanque = float(input('Qual a altura do tanque em metros? '))
comprimentoTanque = float(input('Qual o comprimento do tanque em metros? '))
precoGasolina = float(input('Preço do litro de gasolina em reais: '))
precoAlcool = float(input('Preço do litro de álcool em reais: '))
proporcaoGasolina = float(input('Proporção de gasolina em %: '))
proporcaoAlcool = float(input('Proporção de álcool em %: '))

volumeTanque = larguraTanque * alturaTanque * comprimentoTanque

print(f'Para encher o tanque apenas com gasolina: R$ {precoGasolina * volumeTanque * 1000:.2f}')
print(f'Para encher o tanque apenas com álcool: R$ {precoAlcool * volumeTanque * 1000:.2f}')
print(f'Para encher o tanque na proporção 20% álcool e 80% gasolina: R$ {(precoGasolina * volumeTanque * 1000 * (proporcaoGasolina/100)) + (precoAlcool * volumeTanque * 1000 * (proporcaoAlcool/100)):.2f}')

