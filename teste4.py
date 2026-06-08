#Exercícios a respeito de Funções
"""def somar_numeros(a, b):
    return a + b

resultado = somar_numeros(5, 10)
print(f"A soma de 5 e 10 é: {resultado}")"""

"""def define_number(n):
    if n > 0:
        return "positive number"
    elif n < 0:
        return "negative number"
    else:
        return "zero"
a = 4    
value = define_number(4)
print(f"The number {a} is a {value}.")"""


"""def sum_list(value):
    total = 0
    for v in value:
        total += v
    return total
valores = [100, -50, 200]
resultado = sum_list(valores)
print(f"The sum of the values is: {resultado}")"""

"""def calculate_balance(transactions):
    income = 0
    expense = 0
    for transaction in transactions:
        if transaction["type"] == "income":
            income += transaction["amount"]
        elif transaction["type"] == "expense":
            expense += transaction["amount"]
    return income - expense

transactions = [
    {"amount": 100, "type": "income"},
    {"amount": 50, "type": "expense"}
]
balance = calculate_balance(transactions)
print(f"Final balance: {balance}")"""

"""def finance_resume(transactions):
    income = 0
    expense = 0
    for transaction in transactions:
        if transaction["type"] == "income":
            income += transaction["amount"]
        elif transaction["type"] == "expense":
            expense += transaction["amount"]
    return (
        f"Total income: {income}\n"
        f"Total expense: {expense}\n"
        f"Final balance: {income - expense}"
    )

transactions = [
    {"amount": 100, "type": "income"},
    {"amount": 50, "type": "expense"}
]
balance = finance_resume(transactions)
print(balance)"""

#Learn about f-strings
"""value = 123.2344
print(f"The value is: {value:.3f}")"""

"""value = 1000000
print(f"The value is: {value:,}")"""

"""value = 2340.345
print(f"This is ${value:,.2f}")"""

"""nome = "Aninha"
print(f"{nome:>10}")  # direita
print(f"{nome:<10}")  # esquerda
print(f"{nome:^10}")  # centro
print(f"{nome:.3}")   # truncar a string para 3 caracteres"""

"""def relatorio(entradas, saidas):
    return (
        f"Total de entradas: {entradas}\n"
        f"Total de saídas: {saidas}\n"
        f"Saldo final: {entradas - saidas}"
    )

resultado = relatorio(500, 300)
print(resultado)"""

