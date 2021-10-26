'''
L5. Desempenho do <País> no período que vai desde o <ano 1> até o <ano 2> em
olimpíadas de <Tipo de Olimpíada>, três linhas, uma por cada tipo de medalha.

B11. Quantidade de atletas dos <X> esportes com maior número de atletas na
olimpíada de <Ano> de <Tipo de Olimpíada>.

X9.Quantidade de atletas por esporte nas últimas <X> olimpíadas de <Tipo de
Olimpíada>, um boxplot por cada esporte.

T1. Quantos países participaram da Olimpíada de <Cidade>?


ID_atleta = 'arq_coluna1'
Nome_atleta = 'aqr_coluna2'
Genero_atleta = '(M ou F) arq_coluna3'
Idade_atleta = '(int) arq_coluna4'
Altura_atleta = '(cm) arq_coluna5'
Massa_atleta = '(kg) arq_coluna6'
Equipe = 'arq_coluna7'
Comite_olimpico_nacional = '(sigla) arq_coluna8'
ano_e_temporada = 'arq_coluna9'
ano = '(int) arq_coluna10'
temporada = '(Summer ou Winter) arq_coluna11'
cidade_sede = 'arq_coluna12'
esporte = 'arq_coluna13'
evento = 'arq_coluna14'
medalha = '(Ouro, Prata, Bronze ou NA) arq_coluna15'
'''

#Importar arquivos de planilha
#Separar por linhas e colunas

print('\033[32m*** programa em testes e sujeito a bugs ***' '\n' ' ' '\n' ' ')

opcao_desejada = ''
while True:
  #menu de interação
  print("\033[1m\033[34m•SELECIONE A OPÇÃO DESEJADA: \033[0m" '\n' '\033[1m [1] Gráfico de Linhas' '\n' '\033[1m [2] Gráfico de Barras' '\n' '\033[1m [3] Gráfico Boxplot' '\n' '\033[1m [4] Resposta Textual' '\n' '\033[1m [5] Sair')
  print()
  #escolher opção inicial
  opcao_desejada = input('\033[33m Digite o número da opção: \033[0m').strip()

  print()
  #testar a opção digitada dentre as opções possíveis
  if opcao_desejada == '1':
    print('A opção selecionada foi "Gráfico de Linhas".' '\n' '\033[33mEsta opção irá demonstrar através de um gráfico de linhas o desempenho, em quantidade de medalhas de Ouro, Prata e Bronze, de um certo \033[31mpaís\033[33m, em um determinado \033[31mperíodo de tempo\033[33m e \033[31mtipo de Olimpíada\033[33m.')
    print()

    while True:
      pais = input('Digite o País desejado: ')
      try:
        pais.strip().lower().capitalize()
        #testar se o País digitado está na planilha
        break
      except:
        print('País inválido. Digite o nome de um País válido.')
    pais.strip().lower().capitalize()
    print()

    while True:
      ano1 = input('Digite o ano de início da busca: ')
      try:
        int(ano1)
        #testar se o ano digitado está na planilha
        break
      except:
        print('Ano inválido. Digite um ano válido.' '\n' ' ')
    ano1 = int(ano1)
    print()

    while True:
      ano2 = input('Digite o ano de término da busca: ')
      try:
        int(ano2)
        #testar se o ano digitado está na planilha
        break
      except:
        print('Ano inválido. Digite um ano válido.' '\n' ' ')
    ano2 = int(ano2)
    print()

    while True:
      tipo = input('\033[1m\033[34m•SELECIONE O TIPO DE OLIMPÍADA:' '\n' '\033[0m[1] Olimpíadas de Verão' '\n' '[2] Olimpíadas de Inverno' '\n' '\033[33mDigite o número correspondente ao tipo desejado: \033[0m').strip()
      if tipo == '1':
        tipo = 'Olimpíadas de Verão'
        break
      elif tipo == '2':
        tipo = 'Olimpíadas de Inverno'
        break
      else:
        print('Opção inválida. Digite uma opção válida.')

    print(' ' '\n' 'O País', pais.capitalize()+',', 'nas', tipo, 'conquistou, entre os anos de', ano1, 'e', str(ano2)+':', '\n' ' ' '\n' 'Ano A:' '\n' 'X Medalhas de Ouro' '\n' 'Y Medalhas de Prata' '\n' 'Z medalhas de Ouro')

    print()
    continue
  elif opcao_desejada == '2':
    print('A opção selecionada foi Gráfico de Barras que irá comparar uma quantidade de atletas de determinados esportes, com maior número de atletas na olimpíada em um mesmo ano, de determinado tipo de olimpíada')
    print()
    continue
  elif opcao_desejada == '3':
    print('A opção selecionada foi Gráfico Boxplot,irá comparar a quantidade de atletas por esporte em determinada olimpíada e  de tipo de Olimpíada, onde um boxplot indicará um esporte.')
    print()
    continue
  elif opcao_desejada == '4':
    print('A opção selecionada foi Resposta Textual, que indicará quantos países participaram da Olimpíada em determinada cidade')
    print()
    continue
  elif opcao_desejada == '5':
    print('\033[36mMuito obrigado por testar nosso programa! \033[35mXD' '\n' '\033[36mEsperamos que tenha gostado!' '\n' ' ' '\n' '    \033[31m***CRÉDITOS:***' '\n' '\033[32m ~Isaias Coelho' '\n' ' ~Willyan Gabriel')
    break
  else:
    print('A opção', '"'+str(opcao_desejada)+'"', 'não está entre as disponíveis.' '\n' 'Por favor, selecione uma opção válida.' '\n')