## Desconto progressivo
## < 100 10% entre 101 e 500 15% maior que 500 é 20%
def main():
  print("Desconto progressivo: < 100 10% entre 101 e 500 15% maior que 500 é 20%")
  preco = float(input("Digite o valor da compra: "))
  preco_final = desconto_progressivo(preco)
  print(f"Valor final da compra: ", preco_final)

def desconto_progressivo(valor):
  if valor <= 100:
    desconto1 = valor * 0.1
    vd1 = valor - desconto1
    return vd1
  elif valor >= 101 and valor <= 500:
    desconto2 = valor * 0.15
    vd2 = valor - desconto2
    return vd2
  elif valor > 500:
    desconto3 = valor * 0.2
    vd3 = valor - desconto3
    return vd3
  else:
    print("ERRO! VOCÊ NÃO OBTEVE DESCONTO.")
main()
