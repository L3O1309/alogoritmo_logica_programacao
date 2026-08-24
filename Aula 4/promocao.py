## Aumento no salário 15%
promovido = input("Ganhou a promoção ? (digite sim ou não) ")
salario = float(input("Digite seu salário: "))
promocao = salario * 0.15
salarionovo = salario + promocao
if promovido.lower() == "sim":
  print("Parabéns pela promoção, seu salário agora é: ", salarionovo)
else:
  print("Sinto muito, continue se esforçando!!")
