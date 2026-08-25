## Entrada em evento: 18 anos + ingresso 
idade = int(input("Digite a sua idade: "))
ingresso = input("Possui o ingresso ?")

if ingresso.lower() == "sim" and idade >= 18:
  print("Liberado!")
elif ingresso.lower() == "sim" and idade <= 18:
  print("Não tente me enganar!")
else:
  print("Não pode passar.")
