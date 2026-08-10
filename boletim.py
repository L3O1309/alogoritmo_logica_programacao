print("BOLETIM DE NOTAS")

nome = input("Escreva o nome do(a) aluno(a): ")
discplina = input("Escreva o nome da disciplina: ")
nota = float(input("Digite a nota da disciplina: "))

if nota >= 60 and nota < 101:
    print("Aprovado")

elif nota > 0 and nota < 40:
   print("Reprovado")
   
elif nota >= 40 and nota < 60:
    print("Recuperação")
else:
    print("Nota inválida")
