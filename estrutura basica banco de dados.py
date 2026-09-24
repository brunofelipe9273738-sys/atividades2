def menu():
    print("\x1b[1J\x1b[1;1H")
    print("=================")
    print("1 - Cadastros")
    print("2 - Buscas")
    print("3 - Logout")
    print("=================")

def menu_cadastros():
    print("\x1b[1J\x1b[1;1H")
    print("=================")
    print("1 - Produtos")
    print("2 - Fornecedores")
    print("3 - Usuários")
    print("4 - Voltar")
    print("=================")

def menu_buscar():
    print("\x1b[1J\x1b[1;1H")
    print("=================")
    print("1 - Usuário")
    print("2 - Matrícula")
    print("3 - Nivel")
    print("4 - Voltar")
    print("=================")

while True:

    usuario_bd = "admin"
    senha_bd = "admin@2026"
    produto = []
    user = []

    print("...Digite sair em Usuário ou Senha para encerrar...")
    print("===(LOGIN)===")
    usuario = input("Usuário: ")
    if usuario == "sair":
        break
    password = input("Senha: ")
    if password == "sair":
        break
    if usuario == usuario_bd and password == senha_bd:
        while True:
            menu()
            opcao = int(input("Opção: "))
            match opcao:
                case 1:
                    while True:
                        menu_cadastros()
                        opcao = int(input("Opção: "))
                        match opcao:
                            case 1: 
                                print("\x1b[1J\x1b[1;1H")
                                print("===Cadastro de Produtos===\n")
                                descricao = input("Descrição: ")
                                data_cadastro = input("Data: ")
                                qtd_estoque = int(input("Quantidade Estoque: "))
                                valor_unit = float(input("Preço: "))

                                produto = {
                                    'descricao': descricao,
                                    'data_cadastro': data_cadastro,
                                    'qtd_estoque': qtd_estoque,
                                    'preco': valor_unit
                                }
                                print("\n\n-----------------(Lista)------------------" * 30)
                                print(f"1. Produto:  {produto['descricao']}")
                                print(f"2. Data:  {produto['data_cadastro']}")
                                print(f"3. Quantidade:  {produto['qtd_estoque']}")
                                print(f"4. Preço:  {produto['preco']}")
                                print("----------------------------------------------")
                                op = input("E - Editar \nS - Salvar \nC - Cancelar\n")

                                if (op == 'E') or (op == 'e'):

                                    alt = int(input("Informe o código"))

                                    if alt == 1:
                                        produto['descricao'] = input("Descrição: ")

                                    elif alt == 2:
                                        produto['data_cadastro'] = input("Data de cadastro: ")

                                    elif alt == 3:
                                        produto['qtd_estoque'] = input("Quantidade: ")

                                    elif alt == 4:
                                        produto['preco'] = float(input("Preço: "))

                                    else:
                                        print("Opção Inválida")

                                elif (op == 'S') or (op == 's'):
                                    print("\n\nSalvo com sucesso...")
                                    input("Enter para continuar")
                                    break
                                elif (op == 'C') or (op == 'c'):
                                    print("\n\n")
                                print("\n", produto)

                                input("Enter para continuar...")

                            case 2:
                                print("\x1b[1J\x1b[1;1H")
                                print("===Cadastro de Fornecedores===")
                                input("Enter para continuar...")
                            case 3:
                                print("\x1b[1J\x1b[1;1H")
                                print("===Cadastro de Usuários===")
                                input("Enter para continuar...")
                            case 4:break
                            case _:
                                print("Opção inválida!")
                                input("Enter para continuar...")
           
                case 2:
                    while True:
                        menu_buscar()
                        opcao = int(input("Opção: "))

                        match opcao:

                            case 1:
                                print("\x1b[1J\x1b[1;1H")
                                print("=== Buscar Usuário ===\n")

                                nome = input("Nome: ")
                                nome_usuario = input("Nome de usuario: ")
                                matricula = int(input("Matrícula: "))
                                senha = input("Senha: ")
                                nivel = int(input("Nivel: "))

                                if nivel == 1:
                                    print("Nível: Admin")
                                elif nivel == 0:
                                    print("Nível: Atendente")
                                else:
                                    print("Nível inválido!")

                                user = {
                                    'nome': nome,
                                    'nome_usuario': nome_usuario,
                                    'matricula': matricula,
                                    'senha': senha,
                                    'nivel': nivel
                                }

                                print("\n\n-----------------(Lista)------------------")
                                print(f"1. Nome: {user['nome']}")
                                print(f"2. Nome_usuario: {user['nome_usuario']}")
                                print(f"3. Matrícula: {user['matricula']}")
                                print(f"4. Senha: {user['senha']}")
                                print(f"5. Nivel: {user['nivel']}")
                                print("----------------------------------------------")

                                op = input(
                                    "E - Editar \n"
                                    "S - Salvar \n"
                                    "C - Cancelar\n"
                                )

                                if op == 'E' or op == 'e':

                                    alt = int(input("Informe o código: "))

                                    if alt == 1:
                                        user['nome'] = input("Nome: ")

                                    elif alt == 2:
                                        user['nome_usuario'] = input(
                                            "Nome de usuário: "
                                        )

                                    elif alt == 3:
                                        user['matricula'] = int(
                                            input("Matrícula: ")
                                        )

                                    elif alt == 4:
                                        user['senha'] = input("Senha: ")

                                    elif alt == 5:
                                        user['nivel'] = input("Nivel: ")

                                    else:
                                        print("Opção Inválida")

                                elif op == 'S' or op == 's':
                                    print("\n\nSalvo com sucesso...")
                                    input("Enter para continuar")

                                elif op == 'C' or op == 'c':
                                    print("\n\nCancelado...")
                                    input("Enter para continuar")

                            case 2:
                                print("\x1b[1J\x1b[1;1H")
                                print("=== Buscar por Matrícula ===")

                                matricula_busca = int(
                                    input("Digite a matrícula: ")
                                )

                                if user and user['matricula'] == matricula_busca:
                                    print("\nUsuário encontrado!")
                                    print(f"Nome: {user['nome']}")
                                    print(f"Nome de usuário: {user['nome_usuario']}")
                                    print(f"Matrícula: {user['matricula']}")
                                    print(f"Senha: {user['senha']}")
                                    print(f"nivel: {user['nivel']}")
                                else:
                                    print("\nUsuário não encontrado!")

                                input("Enter para continuar...")

                            case 3:
                                print("\x1b[1J\x1b[1;1H")
                                print("=== Buscar por Nivel ===")
                                input("Enter para continuar...")

                            case 4:
                                break

                            case _:
                                print("Opção inválida!")
                                input("Enter para continuar...")
                case 3:
                    print("Logout realizado!")
                    break

                case _:
                    print("Opção inválida!")
                    input("Enter para continuar...")

    else:
        print("Usuário ou senha inválidos!")