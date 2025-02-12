# ALGORITMO = ENTRADA (INPUT) + PROCESSAMENTO + SAÍDA (PRINT)
"""
Conversão entre unidades: Regra de 3

Centímetro.      Polegada
2.54                 1
comprimento          X

X = comprimento / 2.54
comprimento = comprimento / 2.54

Pés.              Polegada
0.08                 1
  X                comprimento

X = comprimento * 0.08
comprimento = comprimento * 0.08

"""

comprimento = float(input('O comprimento da barra em cm: '))

comprimentoPolegadas = comprimento / 2.54

print(f'O comprimento da barra em polegadas: {comprimentoPolegadas:.2f} polegadas')
print(f'O comprimento da barra em pés: {comprimentoPolegadas * 0.08:.2f} pés')
