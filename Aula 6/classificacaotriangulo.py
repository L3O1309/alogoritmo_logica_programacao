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
    
