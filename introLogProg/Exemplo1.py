'''
O código recebe as medidas e calcula o RCQ
'''

mc = float(input('Qual a medida da sua cintura (cm): '))
mq = float(input('Qual a medida do seu quadril (cm): '))

print(f'O seu RCQ(Relação Cintura-Quadril) é: {(mc/mq)*100 :.2f}%')
