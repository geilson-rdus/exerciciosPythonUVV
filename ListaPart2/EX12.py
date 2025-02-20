try:
    massa = float(input('Informe sua massa em quilogramas: '))
    altura = float(input('Informe sua altura em metros: '))
    
    if(massa <= 0 or altura <= 0):
        print('ERRO: Entrada inválida!')
    else:
        imc = massa / (altura ** 2)
        if(imc < 18.5):
            print(f'Seu IMC {imc: .2f} indica: Magreza')
        elif(imc < 25):
            print(f'Seu IMC {imc: .2f} indica: Saudável')
        elif(imc < 30):
            print(f'Seu IMC {imc: .2f} indica: Sobrepeso')
        elif(imc < 35):
            print(f'Seu IMC {imc: .2f} indica: Obesidade Grau I')
        elif(imc < 40):
            print(f'Seu IMC {imc: .2f} indica: Obesidade Grau II')
        else:
            print(f'Seu IMC {imc: .2f} indica: Obesidade Grau III')
except:
    print('ERRO: Entrada inválida! Digite um número válido para o valor.')
