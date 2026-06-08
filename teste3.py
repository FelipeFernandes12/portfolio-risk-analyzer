"""ponto = (10,20)
ponto[0] = 30 # Isso causará um erro, pois tuplas são imutáveis
print(ponto[0]) # Imprime a coordenada xw"""

"""valores = [100, -50, 0, 300]
for v in valores:  
    if v > 0:
        print(f"Entrada: {v}")
    elif v < 0:
        print(f"Saída: {v}")
    else:
        print("Valor neutro: 0")"""

"""valores = [100, -50, 200, -30]
entrada = 0
for v in valores:
    if v > 0:
        entrada += v
print(f"Total de entradas: {entrada}")"""

"""lancamentos = [
    {"valor": 100, "tipo": "entrada"},
    {"valor": 50, "tipo": "saida"},
    {"valor": 200, "tipo": "entrada"}
]
total = 0
for v in lancamentos:
    total += v["valor"]

    
print (f"Valor atualizado: {total}")"""

"""lancamentos = [
    {"valor": 100, "tipo": "entrada"},
    {"valor": 50, "tipo": "saida"},
    {"valor": 200, "tipo": "entrada"},
    {"valor": 30, "tipo": "saida"}
]
entrada = 0
saida = 0
for v in lancamentos:
    if v["tipo"] == "entrada":
        entrada += v["valor"]
    elif v["tipo"] == "saida":
        saida += v["valor"] 

print(f"Total de entradas: {entrada}")
print(f"Total de saídas: {saida}")  
print(f"Saldo final: {entrada - saida}")"""

"""valores = [5, 10, 15]
a = 0
t = 0
for v in valores:
    t += 1
    a = v*2
    print(f"Valor {t} * 2: {a}")"""

#Exercícios de Laços de Repetição
"""valor = -6
while valor <= 0:
    print(f"Valor negativo: {valor}")
    valor += 1"""

"""valor = 0
while valor < 1000:
    print(f"O saldo é: {valor}, portanto está abaixo de 1000, somaremos + 100 até lá.")
    valor += 100
print(f"O saldo é: {valor}, portanto atingiu ou ultrapassou 1000.")"""

valor = 0
while valor <= 1000:
    if valor < 1000:
        print(f"O saldo é: {valor}, portanto está abaixo de 1000, somaremos + 100 até lá.")
        valor += 100
    else:  # valor == 1000
        print(f"O saldo é: {valor}, portanto atingiu ou ultrapassou 1000.")
        break



        

