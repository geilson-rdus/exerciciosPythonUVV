try:
    unidadeMedida = input('Escreva kg para quilogramas, oz para onça ou ton para dólar: ')
    valorOriginal = float(input('Informe o valor na unidade escolhida: '))
    
    if(valorOriginal < 0):
        print('ERRO: Entrada inválida! Digite um número válido para o valor.')
    else:
        if unidadeMedida.lower() == 'kg':
            conversao1 = valorOriginal * 35.274  
            conversao2 = valorOriginal / 1000  
            print(f'O valor informado em quilogramas foi {valorOriginal:.2f}, que em onças é {conversao1:.2f} e em toneladas é {conversao2:.5f}')
        
        elif unidadeMedida.lower() == 'oz':
            conversao3 = valorOriginal / 35.274  
            conversao4 = conversao3 / 1000  
            print(f'O valor informado em onças foi {valorOriginal:.2f}, que em quilogramas é {conversao3:.2f} e em toneladas é {conversao4:.2f}')
        
        elif unidadeMedida.lower() == 'ton':
            conversao5 = valorOriginal * 1000  
            conversao6 = conversao5 * 35.274   
            print(f'O valor informado em toneladas foi {valorOriginal:.2f}, que em quilogramas é {conversao5:.2f} e em onças é {conversao6:.2f}')
        else:
            print('ERRO: unidade de medida inválida!')
except:
    print('ERRO: Entrada inválida! Digite um número válido para o valor.')
