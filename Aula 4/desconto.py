## Desconto 10% a vista
desconto = input("Digite sim se for pagar a vista: ")
valorcompra = float(input("Digite o valor da compra: "))
valordesconto = valorcompra * 0.10
compracomdesconto = valorcompra + valordesconto
if desconto.lower() == "sim":
  print("O valor da compra com o desconto é: ", compracomdesconto)
else: 
  print("Valor integral: ", valorcompra)
