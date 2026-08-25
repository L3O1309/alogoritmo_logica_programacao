## Senha correta: cadastro + autenticação 
usuario = input("Digite seu nome de usuário: ")
senha = input("Digite sua senha: ")
confirm = input(f"Prezado, {usuario}, digite sua senha novamente para confirmação: ")

if confirm == senha:
  print(f"Seja Bem-Vindo(a) ao sistema Sr. {usuario}")
else:
  print("Algo deu errado, tente novamente!")
