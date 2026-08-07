# senha_correta = input("Digite a senha: ")
# senha = input("Digite a senha correta: ")

# while senha != senha_correta:
#     print("Senha incorreta")
#     senha = input("Digite a senha correta: ")
# print("Seja bem-vindo!")

soma = 0
while True:
    numero = int(input("DIGITE UM NÚMERO: "))
    soma += numero
    if numero == 0:
        break
print(soma)