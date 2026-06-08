def temcaixa(saldo,valor):
    return saldo >= valor

if temcaixa(250, 100):
    print("Tem caixa suficiente para a transação.")
else:
    print("Não tem caixa suficiente para a transação.")