## Desconto progressivo
## < 100 10% entre 101 e 500 15% maior que 500 é 20%
valor = int(input("Digite o valor da compra: "))

if valor <= 100:
  desconto1 = valor * 0.1
  vd1 = valor - desconto1
  print("Deconto de 10% ", vd1)
elif valor >= 101 and valor <= 500:
  desconto2 = valor * 0.15
  vd2 = valor - desconto2
  print("Desconto de 15% ", vd2)
elif valor > 500:
  desconto3 = valor * 0.2
  vd3 = valor - desconto3
  print("Desconto de 20% ", vd3)
else:
  print("ERRO!")
