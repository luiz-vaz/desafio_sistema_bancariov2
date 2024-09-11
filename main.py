from operacoes_bancarias import func_deposito,func_saque,func_extrato
from cliente_contas import func_cadastrar_cliente, func_cliente_duplicado,func_exibir_cliente,func_criar_conta,func_exibir_contas

logo = """
    ===================================================================
                            Vaz Bank
    ===================================================================
"""

menu_inicial = f"""
    {logo}
    Insira opção desejada:

    [a] Gerenciamento de Clientes e Contas
    [b] Operações Bancarias  
    [q] Sair              

=> """

menu_user = f"""
    {logo}
    Bem vindo ao Vaz Bank! Digite a letra correspondente para acessar serviço desejado:

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

=> """

menu_admin = f"""
    {logo}
    Bem vindo ao Vaz Bank! Digite a letra correspondente para acessar serviço desejado:

    [u] Cadastrar Cliente
    [c] Criar Conta Corrente
    [p] Lista de Clientes
    [x] Lista de Contas
    [q] Sair

=> """

saldo_atual = 0
extrato = ""
saques_feitos = 0
contador_numero_conta = 0
      
    
while True:

    opcao =input(menu_inicial).lower()

    if opcao == "b":
        while True:    

            opcao=input(menu_user).lower()

            if opcao == "d":   
                saldo_atual, extrato =func_deposito(saldo_atual,extrato)                
            elif opcao == "s":
                saldo_atual, extrato, saques_feitos  =func_saque(saldo_atual=saldo_atual, extrato=extrato,saques_feitos=saques_feitos)                
            elif opcao == "e":
                func_extrato(saldo_atual,extrato=extrato)
            elif opcao == "q":
                break
            else:
                print("Opção Inválida!!!!!!")

    elif opcao == "a":

        while True:

            opcao=input(menu_admin).lower()

            if opcao == "u":
                func_cadastrar_cliente()
            elif opcao == "c":
                contador_numero_conta=func_criar_conta(contador_numero_conta)
                print(f"contador de conta: {contador_numero_conta}")
            elif opcao == "p":
                print(logo)
                func_exibir_cliente()
            elif opcao == "x": 
                print(logo)               
                func_exibir_contas()
            elif opcao == "q":
                break
            else:
                print("Opção Inválida!!!!!!")

    elif opcao == "q":
                break
    else:
        print("Opção Inválida!!!!!!")
