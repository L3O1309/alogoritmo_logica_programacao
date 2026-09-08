## Opções de forma de pagamento
lista = ["1. À Vista", "2. Crédito", "3. Parcelado 2x sem juros", "4. Parcelado 3x com juros"]
print("Suas opções de compras são: ", lista)
escolha = int(input("Escolha uma forma de pagamento de acordo com o número antes da forma (1, 2, 3, 4): "))
if escolha == 1:
  print("Forma de pagamento:", lista[0])
elif escolha == 2:
  print("Forma de pagamento:", lista[1])
elif escolha == 3:
  print("Forma de pagamento:", lista[2])
elif escolha == 4:
  print("Forma de pagamento:", lista[3])
else:
  print("ERRO!")
