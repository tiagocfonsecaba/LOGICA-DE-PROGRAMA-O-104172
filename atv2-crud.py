import os

lista_jogador = []

while True:
  # 'cls' funciona no Windows. Se usar Linux/Mac, o ideal é 'clear'
  os.system('cls')

  print('''
=== Cadastro de jogadores ===
1. Cadastrar jogador
2. Listar jogadores
3. Atualizar jogadores
4. Excluir jogadores
0. Sair''')

  opcao = int(input("Escolha a opção desejada:  "))

  match opcao:

    case 1:
      print("\n== Registre o jogador ==")
      nome_jogador = (input("Digite o nome do jogador a ser registrado: ").strip().upper()
      )

      if nome_jogador == "":
        print("O nome do jogador deve ser inserido....")
      elif nome_jogador in lista_jogador:
        print("Jogador já está registrado.")
      else:
        lista_jogador.append(nome_jogador)
        print("Jogador registrado com sucesso!")

      input("\nPressione Enter para continuar...")

    case 2:
      print("\n== Lista de jogadores ==")
      if not lista_jogador:
        print("Nenhum jogador cadastrado ainda.")
      else:
        for jogador in lista_jogador:
          print(f"- {jogador}")
        # O total fica fora do 'for' para aparecer apenas uma vez no final
        print(f"\nTotal: {len(lista_jogador)}")

      input("\nPressione Enter para continuar...")

    case 3:
      print("\n== Atualizar jogador ==")
      jogador_antigo = (
          input("Digite o nome do jogador que deseja alterar: ")
          .strip()
          .upper()
      )

      if jogador_antigo in lista_jogador:
        novo_nome = (
            input(f"Digite o novo nome para {jogador_antigo}: ")
            .strip()
            .upper()
        )

        if novo_nome == "":
          print("O nome não pode ser vazio.")
        elif novo_nome in lista_jogador:
          print("Este novo nome já pertence a outro jogador registrado.")
        else:
          # Encontra a posição do jogador antigo e substitui pelo novo nome
          indice = lista_jogador.index(jogador_antigo)
          lista_jogador[indice] = novo_nome
          print("Jogador atualizado com sucesso!")
      else:
        print("Jogador não encontrado.")

      input("\nPressione Enter para continuar...")

    case 4:
      print("\n== Excluir jogador ==")
      jogador_excluir = (input("Digite o nome do jogador que deseja excluir: ").strip().upper())

      if jogador_excluir in lista_jogador:
        lista_jogador.remove(jogador_excluir)
        print(f"Jogador {jogador_excluir} excluído com sucesso!")
      else:
        print("Jogador não encontrado.")

      input("\nPressione Enter para continuar...")

    case 0:
      print("\nSaindo do programa... Até logo!")
      break

    case _:
      print("\nOpção inválida! Escolha um número de 0 a 4.")
      input("\nPressione Enter para continuar...")
