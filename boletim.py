print("BOLETIM DE NOTAS")

nome = input("\nEscreva o nome do(a) aluno(a): ")
curso = input("Escreva o nome do curo: ")
disciplina = input("Escreva o nome da disciplina: ")
semestre = int(input("Digite o semestre em que está: "))
nota1 = float(input("Digite a nota do primeiro bimestre da disciplina: "))
nota2 = float(input("Digite a nota do segundo bimestre da disciplina: "))

media = (nota1 + nota2) / 2

print("\nNome: ", nome)
print("Curso: ", curso)
print("Disciplina: ", disciplina)
print(semestre, "º Semestre")
print("Média: ", media)



if media >= 60 and media < 101:
    print("\nAprovado")

elif media > 0 and media < 40:
   print("\nReprovado")
   
elif media >= 40 and media < 60:
    print("\nRecuperação")
else:
    print("\nNota inválida")
