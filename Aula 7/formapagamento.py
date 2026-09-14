## Opções de forma de pagamento
lista = ["1. À Vista", "2. Crédito", "3. Parcelado 2x sem juros", "4. Parcelado 3x com juros"]
def processar_pagamento(escolha):
  match escolha:
    case 1:
      print("Sua opção escolhida foi: ", lista[0])
    case 2:
      print("Sua opção escolhida foi: ", lista[1])
    case 3:
      print("Sua opção escolhida foi: ", lista[2])
    case 4:
      print("Sua opção escolhida foi: ", lista[3])
    case _: 
      print("ERRO!")

print("Suas opções de compras são: ", lista)
opcao_escolhida = int(input("Escolha uma forma de pagamento de acordo com o número antes da forma (1, 2, 3, 4): "))
processar_pagamento(opcao_escolhida)
