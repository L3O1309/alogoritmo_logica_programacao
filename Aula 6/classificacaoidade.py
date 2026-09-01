## Classificação Criança, Adolescente, Adulto e Idoso
age = int(input("Digite sua idade: "))

if age < 12:
  print("Criança!")
elif age >= 12 and age < 18:
  print("Adolescente")
elif age >=18 and age < 60:
  print("Adulto")
else:
  print("Idoso")


