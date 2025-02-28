try:
    n1 = float(input('Insira um número real: '))
    n2 = float(input('Insira um número real: '))
    n3 = float(input('Insira um número real: '))

    media = (n1 + n2 + n3) / 3
    if(media < (10 * 11.52743) or media > (200 * 11.52743)):
        cuboMedia = media ** 3
        print(f'O cubo da média: {cuboMedia: .5f}')
    else:
        print('Os números não se adequaram as exigências')
except Exception as ERRO_EXCECAO:
  print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')
