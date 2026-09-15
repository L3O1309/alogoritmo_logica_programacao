"""Como não fizemos nada além da correção
   , vou fazer um código nada haver aqui"""
def helloworld():
  print("Hello World!")
def olaestudante():
  print("Olá Estudante!")
def semanaprovas():
  print("Semana de provas logo aí")
decida = int(input("Digite um número de 1-3 para exibir uma mensagem no terminal: "))
match decida:
  case 1:
    helloworld()
  case 2:
    olaestudante()
  case 3:
    semanaprovas()
  case _:
    print("Ocorreu um erro, tente novamente!")
