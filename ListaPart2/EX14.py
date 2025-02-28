try:
  AV1 = float(input('Insira o valor da primeira prova [0,10]: '))
  AV2 = float(input('Insira o valor da segunda prova [0,10]: '))
  cargaHoraria = int(input('Insira a carga horária da disciplina(40, 60 ou 80): '))
  TF = int(input('Insira a quantidade de faltas do aluno em horas: '))
  if(AV1 < 0 or AV1 > 10 or AV2 < 0 or AV2 > 10):
    print('ERRO: Você inseriu valores menores que 0 ou maiores que 10 para pelo menos uma das provas')
  elif(cargaHoraria != 40 and cargaHoraria != 60 and cargaHoraria != 80):
    print('ERRO: Você inseriu um valor inválido para carga horária')
  elif(TF < 0):
    print('ERRO: Você inseriu um valor inválido para o total de faltas')
  else:
    porcentagemFaltas = TF/cargaHoraria * 100
    if(porcentagemFaltas > 100):
      print('ERRO: Você inseriu um valor para o total de faltas maior do que a carga horária')
    elif(porcentagemFaltas > 25):
      print('Aluno reprovado por faltas')
    else:
      MP = round((AV1 + AV2)/2,1)
      if(MP < 3):
        print(f'A MP do aluno foi {MP:.1f}: Aluno reprovado')
      elif(MP < 7):
        print(f'A MP do aluno foi {MP:.1f}: Aluno de prova final')
        AVF = float(input('Insira o valor da prova final [0,10]: '))
        if(AVF < 0 or AVF > 10):
          print('ERRO: Você inseriu valores menores que 0 ou maiores que 10 para a prova final')
        else:
          MF = round((MP + AVF) / 2,1)
          if(MF < 5):
            print(f'A MF do aluno foi {MF:.1f}: Aluno reprovado')
          else:
            print(f'A MF do aluno foi {MF:.1f}: Aluno aprovado')
      else:
        print(f'A MP do aluno foi {MP:.1f}: Aluno aprovado')

except Exception as ERRO_EXCECAO:
  print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')
