## Maior entre três números
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))

if n1 > n2 and n1 > n3:
  print("Primeiro é maior!")
elif n2 > n1 and n2 > n3:
  print("Segundo é maior!")
else:
  print("Terceiro é maior!")
