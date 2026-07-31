item = float(input("Digite o valor do item da compra: "))
salario = 100

if item > salario:
    soma = item + salario
    desconto = soma * 10
    print(f"valor da compra: {desconto}")
else:
    print(f"valor original: {item}")