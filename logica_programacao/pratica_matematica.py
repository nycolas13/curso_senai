nome = input("NOME: ")
telefone = input("TELEFONE: ")
cpf = input("CPF: ")
salario = float(input("Valor do salário que recebe mensalmente: "))

mult = salario * 12
print(f"""
    NOME: {nome},
    TELEFONE: {telefone},
    CPF: {cpf},
    SALÁTIO: {salario},
    TOTAL do SALÁRIO: {mult}
    """)