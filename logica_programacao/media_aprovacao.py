materia1 = float(input("Digite a nota desse aluno: "))
materia2 = float(input("Digite a nota desse aluno: "))
materia3 = float(input("Digite a nota desse aluno: "))

media = (materia1 + materia2 + materia3) / 3

if media >= 7:
    print("Aprovado")
elif media >= 5:
    print("Recuperação")
else:
    print("Reprovado")