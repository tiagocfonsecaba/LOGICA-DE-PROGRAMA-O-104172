import os


lista_paciente = []

while True:
    os.system('cls')
    print('''
=== Hospital Gotei 13 ===
1. Cadastrar paciente
2. Listar pacientes
3. Atualizar paciente
4. Excluir paciente
0. Sair''')

    opcao = int(input('Escolha uma opção: '))

    match opcao:
            case 1:
    
                print('\n== CADASTRAR PACIENTE ==')
                nome_paciente = input('Digite o nome do paciente: ').strip().upper()
                sobrenome_paciente = input('Digite o sobrenonome do paciente: ').strip().upper()
                
                if nome_paciente == '':
                    print("O nome do paciente deve ser inserido....")
                    
                elif nome_paciente in lista_paciente:
                
                    print('Paciente ja cadastrado.')
                else:
                    lista_paciente.append((nome_paciente,sobrenome_paciente))
                    print('Paciente cadastrado com sucesso!')

            case 2:
                
                print('\n== PACIENTES CADASTRADOS ==')
                for paciente in lista_paciente:
                    
                    print (f'- {paciente}')
                print(f'Total: {len(lista_paciente)}')

                input("Pressione uma tecla para continuar")

            case 3:

                print('\n== ATUALIZAR PACIENTE ==')
                nome = input('Qual paciente deseja atualizar?: ')
                if nome in lista_paciente:
                    posicao = lista_paciente.index(nome)
                    novo = input('Novo nome: ')
                    lista_paciente[posicao] = novo
                    print('Paciente atualizado com sucesso!')

            case 4:
                    
                    print('\n== REMOVER CADASTRO  ==')
                    nome = input('Qual paciente deseja remover?: ')
                    if nome in lista_paciente:
                        lista_paciente.remove(nome)
                        print('Paciente excluido com sucesso!')
                    else:
                        print('Paciente não encontrado.')
        
            case 5:
                    print('== ENCONTRAR PACIENTE ==')
                    nome = input('Qual paciente deseja buscar?: ')
                    if nome in lista_paciente:
                        print('Paciente encontrado!')
                    else:
                        print('Este paciente não esta cadastrado.')
            case 0:
                    print('Saido do programa...')
                    break
        
            case _:
                    print('Opção inválida! \nTente novamente...')
                    input('Pressione uma tecla para continuar...')