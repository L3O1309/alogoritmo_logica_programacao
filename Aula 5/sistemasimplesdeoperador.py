## Calculadora simples
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
operacao = input("Digite a operação (soma, subtração, divisão e multiplicação) ")
soma = n1 + n2
sub = n1 - n2
div = n1 / n2
mult = n1 * n2


if operacao.lower() == "soma":
  print(f"A soma de {n1} + {n2} é: ", soma )
elif operacao.lower() == "subtração":
  print(f"A subtração de {n1} - {n2} é: ", sub)
elif operacao.lower() == "divisão":
  print(f"A divisão de {n1} / {n2} é: ", div)
elif operacao.lower() == "multiplicação":
  print(f"A multiplicação de {n1} * {n2} é: ", mult)
else:
  print("Apenas as 4 principais operações entre dois números!")
