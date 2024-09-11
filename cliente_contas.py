usuarios = []
contas = []

def func_cliente_duplicado(cpf):
    duplicado = False
    for user in usuarios:
        if user['cpf'] == cpf:
            duplicado = True
    return duplicado

def func_cadastrar_cliente():
    cpf = input("Insira o valor de CPF para cadastrar novo cliente:")

    duplicado=func_cliente_duplicado(cpf)

    if duplicado is True:
        print("CPF inválido - Usuário ja possui cadastro!")
    else:
        nome = input("Insira o nome:")
        data_nascimento = input("Insira a data de nascimento:")
        endereco = input("Insira o endereço:")

        usuario = {
            "cpf": cpf,
            "nome": nome,
            "data de nascimento":data_nascimento,
            "endereco":endereco        
        }

        usuarios.append(usuario)

def func_exibir_cliente(): 
    if not usuarios:
        print("Não ha nenhum cliente cadastrado")
    else:
        for user in usuarios:
            print(f"==> Nome: {user['nome']}, CPF: {user['cpf']}, Data de Nascimento: {user['data de nascimento']}, Endereço: {user['endereco']} <==\n")

def func_criar_conta(contador_numero_conta):
    agencia = "0001"     

    cpf = input("Insira o cpf para vincular a conta:")

    for user in usuarios:        
        if user['cpf'] == cpf:
            nome = user['nome']

            print(f"Cliente encontrado - Nome: {nome}")

            contador_numero_conta += 1

            while True:

                opcao=int(input(f"Qual é o tipo de conta:\n1) Básico\n2) Normal\n3) Premium\n=>>"))

                if opcao == 1:
                    tipo = "basico"
                    break
                elif opcao == 2:
                    tipo = "normal"
                    break
                elif opcao == 3:
                    tipo = "premium"
                    break
                else:
                    print("OPÇÃO INVÁLIDA - Favor digite uma opção válida!!")

            conta = {

                "agencia":agencia,
                "conta":contador_numero_conta,
                "usuario":nome,
                "cpf":cpf,
                "tipo":tipo
            }
            contas.append(conta)
        else:
            print("Não é possivel abrir uma conta sem um cliente cadastrato!!")

    return contador_numero_conta

def func_exibir_contas():
    
    while True:

        if not contas:
                print("Não há contas cadastradas")
                break
        else:
            opcao = int(input("Digite a opção desejada:\n1) Listar todas as contas\n2) Listar Contas de Usuário\n==>"))
            if opcao == 1:               
                for conta in contas:
                    print(f"==> Agência: {conta['agencia']}, Númera da conta: {conta['conta']}, Usuário: {conta['usuario']}, CPF:{conta['cpf']}, Tipo da Conta: {conta['tipo']} <==\n")
                break
            elif opcao ==2:
                cpf= str(input("Por favor, informe o seu CPF para que possamos listar as suas contas: "))             
                cliente_cadastrado=func_cliente_duplicado(cpf)
                if cliente_cadastrado == True:            
                    for conta in contas:
                        if cpf == conta['cpf']:
                            print(f"==> Agência: {conta['agencia']}, Númera da conta: {conta['conta']}, Usuário: {conta['usuario']}, CPF:{conta['cpf']}, Tipo da Conta: {conta['tipo']} <==\n")
                    break
                else:
                    print("CPF invalido: Não existe cliente com CPF informado")
            else:
                print("OPÇÃO INVÁLIDA - Favor digite uma opção válida!!")    