programa {
  funcao inicio() {

    escreva ("CLASSIFICAÇÃO DE UM TRIÂNGULO QUALQUER! \n")

    real lado_1, lado_2, lado_3

    escreva ("\nEscreva o valor do primeiro lado do triângulo: ")
    leia (lado_1)
    escreva ("Escreva o valor do segundo lado do triângulo: ")
    leia (lado_2)
    escreva ("Escreva o valor do terceiro lado do triângulo: ")
    leia (lado_3)

    se ((lado_1 == lado_2) e (lado_2 == lado_3))
    {
      escreva ("\nEste triângulo é equilátero!")
    }
    senao se ((lado_1 == lado_2 e lado_1 != lado_3) ou (lado_2 == lado_3 e lado_2 != lado_1) ou (lado_1 == lado_3 e lado_1 != lado_2))
    {
      escreva ("\nEste triângulo é isósceles!")
    }
    senao
    {
      escreva ("\nEste triângulo é escaleno!")
    }
  }
}
