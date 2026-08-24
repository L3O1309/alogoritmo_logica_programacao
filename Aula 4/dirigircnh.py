## Pode dirigir se tiver cnh
idade = int(input("Digite sua idade: "))
cnh = input("Possui cnh ? ") 

if cnh.lower() == "sim" and idade >= 18:
  print("Pode dirigir")
elif cnh.lower() == "sim" and idade <= 18:
  print("Não minta!")
else:
  print("Não pode dirigir")
