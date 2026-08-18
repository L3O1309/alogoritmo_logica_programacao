## Quem pode votar
idade = float(input("Digite sua idade: "))

if idade >= 16 and idade < 18:
  print("Pode votar, mas não é obrigatório!")
elif idade >=18:
  print("Precisa votar!")
else:
  print("Não pode votar!")
