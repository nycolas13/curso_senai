saldo = int(input("Digite o seu saldo: "))
valor_saque = int(input("Digite o quanto vc quer sacar: "))

if valor_saque > 20:
    pergunta = input("Ha saldo suficiente para realizar o saque?: (S/N): ")
    if pergunta == "S":
        sub = valor_saque - saldo
        print(f"VALOR TOTAL: {sub}")
    elif pergunta == "N":
        print("Não tem como sacar!")
