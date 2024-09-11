def func_deposito(saldo,extrato,/):

    data = "04/09/2024"
    valor_deposito = 0      

    valor_deposito= float(input("Deposito - Por favor insira o valor: R$"))

    if valor_deposito <= 0:
        print(f"Depósito inválido!!! Valor de R${valor_deposito:.2f} não é válido\n")
        
    else:
        print(f"Valor de R$ {valor_deposito:.2f} foi depositado com Sucesso!!\n")
        extrato += f"Depósito(+) de R${valor_deposito:.2f} no dia {data}\n"
        saldo += valor_deposito  

    return saldo, extrato
   
def func_saque(*,saldo_atual,extrato,saques_feitos):   
    limite_por_saque = 500  
    LIMITE_DIARIO = 3  
    
    data = "04/09/2024"

    valor_saque = float(input("Saque - Por favor insira o valor: R$"))

    if saques_feitos >= LIMITE_DIARIO:
        print("Atenção: Limite de Saque Diário Atingido") 
        
    elif valor_saque > saldo_atual:
        print("Não foi possivel realizar operação - SALDO INSUFICIENTE")        
          
    elif valor_saque > limite_por_saque:
        print(f"Valor de saque maior que limite da conta->R${limite_por_saque:.2f}")
        
    elif valor_saque <= saldo_atual and valor_saque < limite_por_saque:
        saldo_atual -= valor_saque        
        print(f"Saque no valor de R${valor_saque:.2f} foi realizado com sucesso")
        extrato += f" Saque(-) de R${valor_saque:.2f} no dia {data}\n"
        saques_feitos +=1
        
    return saldo_atual, extrato, saques_feitos
    

def func_extrato(saldo_atual,/,*,extrato):
   
    if extrato == "":
        print("*"*20,"EXTRATO","*"*20,"\n",f"Não há transações registradas\n Seu Saldo Atual: R$ {saldo_atual:.2f}\n","*"*48)
    else:      
        print("*"*20,"EXTRATO","*"*20,"\n",f"{extrato} Seu Saldo Atual: R$ {saldo_atual:.2f}\n","*"*48)
    return extrato