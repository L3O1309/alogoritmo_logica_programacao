def ex1():
  print("BOLETIM DE NOTAS")
  
  nome = input("\nEscreva o nome do(a) aluno(a): ")
  curso = input("Escreva o nome do curo: ")
  disciplina = input("Escreva o nome da disciplina: ")
  semestre = int(input("Digite o semestre em que está: "))
  nota1 = float(input("Digite a nota do primeiro bimestre da disciplina: "))
  nota2 = float(input("Digite a nota do segundo bimestre da disciplina: "))
  
  media = (nota1 + nota2) / 2
  
  print("\nNome: ", nome)
  print("Curso: ", curso)
  print("Disciplina: ", disciplina)
  print(semestre, "º Semestre")
  print("Média: ", media)
  
  
  
  if media >= 60 and media < 101:
      print("\nAprovado")
  
  elif media > 0 and media < 40:
     print("\nReprovado")
     
  elif media >= 40 and media < 60:
      print("\nRecuperação")
  else:
      print("\nNota inválida")
def ex2():
  ##Aula 2 Ex 3
  print("ANTECESSOR E SUCESSOR")
  n = float(input("Escreva um número: "))

  ant = n - 1
  suc = n + 1

  print("Antecessor: ", ant)
  print("Sucessor: ", suc)
def ex3():
  ##Aula 2 Ex 4
  print("ÁREA DO TRIANGULO")

  b = float(input("Digite a b do triangulo: "))
  h = float(input("Digite a h do triangulo: "))
  area = (b*h) /2

  print("Área: ", area)

def ex4():
  print("DIVISÃO")
  a = float(input("Escreva um número: "))
  b = float(input("Escreva um número: "))

  div = a / b

  print("Divisão: ", div)

def ex5():
  print("DOBRO E TRIPLO")
  n = float(input("Escreva um número: "))

  dob = n * 2
  tri = n * 3

  print("Dobro: ", dob)
  print("Triplo: ", tri)


def ex6():
  print("MULTIPLICAÇÃO")
  a = float(input("Escreva um número: "))
  b = float(input("Escreva um número: "))

  mult = a * b

  print("Multiplicação: ", mult)


def ex7():
  print("PERÍMETRO DO RETÂNGULO")

  b = float(input("Digite a b do triangulo: "))
  h = float(input("Digite a h do triangulo: "))

  p = 2*(b+h)

  print("Perímetro: ", p)


def ex8():
  print("SOMA")
  a = float(input("Escreva um número: "))
  b = float(input("Escreva um número: "))

  soma = a + b


  print("Soma: ", soma)


def ex9():
  print("SUBTRAÇÃO")
  a = float(input("Escreva um número: "))
  b = float(input("Escreva um número: "))

  sub = a - b

  print("Subtração", sub)

def ex10():
  ## Maior entre dois números
  n1 = float(input("Digite um número: "))
  n2 = float(input("Digite outro número: "))

  if n1 > n2:
    print("Primeiro número é maior!")
  else: 
    print("Segundo número é maior!")


def ex11():
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


def ex12():
  ## Par ou Ímpar
  n = float(input("Digite um número: "))

  if (n % 2) == 0:
    print("Número Par!")
  else:
    print("Número Ímpar!")


def ex13():
  ## Positivo, negativo ou zero
  n = float(input("Digite um número: "))

  if n > 0:
    print("Número Positivo!")
  elif n < 0:
    print("Número Negativo!")
  else:
    print("Igual a zero!")


def ex14():
  ## Quem pode dirigir
  idadep1 = float(input("Digite a idade da primeira pessoa: "))
  idadep2 = float(input("Digite a idade da segunda pessoa: "))
  idadep3 = float(input("Digite a idade da terceira pessoa: "))

  if idadep1 >= 18:
    print("Primeira idade pode votar!")
  else: 
    print("Primeira idade não pode votar!")
  if idadep2 >= 18:
    print("Segunda idade pode votar!")
  else: 
    print("Segunda idade não pode votar!")
  if idadep3 >= 18:
    print("Terceira idade pode votar!")
  else: 
    print("Terceira idade não pode votar!")
  ##Dava pra facilitar, mas o professor preferia assim


def ex15():
  ## Quem pode votar
  idade = float(input("Digite sua idade: "))

  if idade >= 16 and idade < 18:
    print("Pode votar, mas não é obrigatório!")
  elif idade >=18:
    print("Precisa votar!")
  else:
    print("Não pode votar!")


def ex16():
  ## Desconto 10% a vista
  desconto = input("Digite sim se for pagar a vista: ")
  valorcompra = float(input("Digite o valor da compra: "))
  valordesconto = valorcompra * 0.10
  compracomdesconto = valorcompra + valordesconto
  if desconto.lower() == "sim":
    print("O valor da compra com o desconto é: ", compracomdesconto)
  else: 
    print("Valor integral: ", valorcompra)


def ex17():
  ## Pode dirigir se tiver cnh
  idade = int(input("Digite sua idade: "))
  cnh = input("Possui cnh ? ") 

  if cnh.lower() == "sim" and idade >= 18:
    print("Pode dirigir")
  elif cnh.lower() == "sim" and idade <= 18:
    print("Não minta!")
  else:
    print("Não pode dirigir")


def ex18():
  ## Aumento no salário 15%
  promovido = input("Ganhou a promoção ? (digite sim ou não) ")
  salario = float(input("Digite seu salário: "))
  promocao = salario * 0.15
  salarionovo = salario + promocao
  if promovido.lower() == "sim":
    print("Parabéns pela promoção, seu salário agora é: ", salarionovo)
  else:
    print("Sinto muito, continue se esforçando!!")


def ex19():
  ## Senha correta: cadastro + autenticação 
  usuario = input("Digite seu nome de usuário: ")
  senha = input("Digite sua senha: ")
  confirm = input(f"Prezado, {usuario}, digite sua senha novamente para confirmação: ")

  if confirm == senha:
    print(f"Seja Bem-Vindo(a) ao sistema Sr. {usuario}")
  else:
    print("Algo deu errado, tente novamente!")


def ex20():
  ## Entrada em evento: 18 anos + ingresso 
  idade = int(input("Digite a sua idade: "))
  ingresso = input("Possui o ingresso ?")

  if ingresso.lower() == "sim" and idade >= 18:
    print("Liberado!")
  elif ingresso.lower() == "sim" and idade <= 18:
    print("Não tente me enganar!")
  else:
    print("Não pode passar.")


def ex21():
  ## Intervalo de 10 a 50
  num = float(input("Digite um número no intevalo de 10 a 50: "))

  if num >= 10 and num <= 50:
    print("Tudo certo!")
  else:
    print("Não está no intevalo, tente novamente!")


def ex22():
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


def ex23():
  ## Está chovendo ?
  chuva = input("Está chovendo agora ?(sim/não) ").lower().strip()

  if chuva == "sim" or chuva == "yes":
    print("Está chovendo, leve um guarda-chuva!")
  else:
    print("Não está chovendo, guarde o guarda-chuva.")


def ex24():
  ## Classificação Criança, Adolescente, Adulto e Idoso
  age = int(input("Digite sua idade: "))

  if age < 12:
    print("Criança!")
  elif age >= 12 and age < 18:
    print("Adolescente")
  elif age >=18 and age < 60:
    print("Adulto")
  else:
    print("Idoso")

def ex25():
  ## Classificação de triângulos
  lado_1 = float(input("Digite o primeiro lado: "))
  lado_2 = float(input("Digite o segundo lado: "))
  lado_3 = float(input("Digite o terceiro lado: "))

  if (lado_1 == lado_2) and (lado_2 == lado_3):
    print("\nEste triângulo é equilátero!")
    
  elif (lado_1 == lado_2 and lado_1 != lado_3) or (lado_2 == lado_3 and lado_2 != lado_1) or (lado_1 == lado_3 and lado_1 != lado_2):
    print("\nEste triângulo é isósceles!")
      
  else:
    print ("\nEste triângulo é escaleno!")
      
def ex26():
  ## Prática esportiva liberada com autorização e se tiver entre 12 a 18 anos 
  idade = int(input("Digite sua idade: "))
  autorizacao = input("Você tem autorização ? (sim/não)").lower().strip()
  if (idade >= 12 and idade <= 18 and autorizacao == "sim"):
    print("Liberado!")
  else:
    print("Não liberado!")

def ex27():
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
def ex28():
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


def ex29():
  print("Executando exercício 29")


def ex30():
  print("Executando exercício 30")

escolha = int(input("Selecione um número de exercício: "))
match escolha:
  case 1:
    ex1()
  case 2:
    ex2()
  case 3:
    ex3()
  case 4:
    ex4()
  case 5:
    ex5()
  case 6:
    ex6()
  case 7:
    ex7()
  case 8:
    ex8()
  case 9:
    ex9()
  case 10:
    ex10()
  case 11:
    ex11()
  case 12:
    ex12()
  case 13:
    ex13()
  case 14:
    ex14()
  case 15:
    ex15()
  case 16:
    ex16()
  case 17:
    ex17()
  case 18:
    ex18()
  case 19:
    ex19()
  case 20:
    ex20()
  case 21:
    ex21()
  case 22:
    ex22()
  case 23:
    ex23()
  case 24:
    ex24()
  case 25:
    ex25()
  case 26:
    ex26()
  case 27:
    ex27()
  case 28:
    ex28()
  case 29:
    ex29()
  case 30:
    ex30()
  case _:
    print("Exercício inválido!")
