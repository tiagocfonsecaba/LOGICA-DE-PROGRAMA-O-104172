import os
os.system("cls")

# Variáveis para armazenar os dados da pesquisa
total_pessoas = 0
soma_salarios = 0.0
maior_idade = 0
menor_idade = 0
qtd_mulheres_salario_alto = 0

# Flag para verificar se há dados cadastrados
primeiro_cadastro = True

while True:
  print('\n=== MENU DE PESQUISA ===')
  print('1. Adicionar pessoa')
  print('2. Exibir resultados')
  print('3. Sair do programa')

  opcao = input('Escolha uma opção (1-3): ')
  if opcao == '1':
    print('\n--- ADICIONAR PESSOA ---')

    # Leitura da idade
    try:
      idade = int(input('Digite a idade: '))
    except ValueError:
      print('Idade inválida! Digite um número inteiro.')
      continue

    # Leitura do sexo
    sexo = input('Digite o sexo (M ou F): ').upper()
    while sexo != 'M' and sexo != 'F':
      print('Sexo inválido! Digite apenas M ou F.')
      sexo = input('Digite o sexo (M ou F): ').upper()

    # Leitura do salário
    try:
      salario = float(input('Digite o salário (R$): '))
    except ValueError:
      print('Salário inválido! Digite um valor numérico.')
      continue

    # Atualização dos dados estatísticos
    if primeiro_cadastro:
      maior_idade = idade
      menor_idade = idade
      primeiro_cadastro = False
    else:
      if idade > maior_idade:
        maior_idade = idade
      if idade < menor_idade:
        menor_idade = idade

    soma_salarios += salario
    total_pessoas += 1

    # Verificar mulheres com salário a partir de 5000
    if sexo == 'F' and salario >= 5000.0:
      qtd_mulheres_salario_alto += 1

    print('Pessoa adicionada com sucesso!')

  elif opcao == '2':
    print('\n=== RESULTADOS DA PESQUISA ===')
    if total_pessoas > 0:
      media_salario = soma_salarios / total_pessoas
      print(f'Média de salário do grupo: R$ {media_salario:.2f}')
      print(f'Maior idade do grupo: {maior_idade} anos')
      print(f'Menor idade do grupo: {menor_idade} anos')
      print(
          'Quantidade de mulheres com salário a partir de R$ 5.000,00:'
          f' {qtd_mulheres_salario_alto}'
      )
      print(f'Total de pessoas entrevistadas: {total_pessoas}')
    else:
      print('Nenhum dado cadastrado até o momento.')

  elif opcao == '3':
    print('Saindo do programa. Até logo!')
    break
  else:
    print('Opção inválida! Escolha 1, 2 ou 3.')
