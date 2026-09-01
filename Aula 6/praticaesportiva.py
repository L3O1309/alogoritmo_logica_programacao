## Prática esportiva liberada com autorização e se tiver entre 12 a 18 anos 
idade = int(input("Digite sua idade: "))
autorizacao = input("Você tem autorização ? (sim/não)").lower().strip()
if (idade >= 12 and idade <= 18 and autorizacao == "sim"):
  print("Liberado!")
else:
  print("Não liberado!")
