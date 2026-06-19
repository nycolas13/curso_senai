nome = input("Nome do aluno: ")
prof = input("Nome do professor: ")
turma = input("Turma do aluno: ")
materia = input("Matérias do professor: ")
nota1 = float(input("Nota da primeira matéria: "))
nota2 = float(input("Nota da segunda matéria: "))
nota3 = float(input("Nota da terceira matéria: "))

soma_notas = (nota1 + nota2 + nota3) / 3

print(f"""
        NOME do ALUNO: {nome},
        NOME do PROFESOR: {prof},
        TURMA do ALUNO: {turma},
        MATÉRIA: {materia},
        MÉDIA: {soma_notas}
        """)