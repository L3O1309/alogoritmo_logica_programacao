programa {
  funcao real media(real nota1, real nota2){
    retorne (nota1 + nota2) / 2
  }
  funcao inicio() {
    real n1
    real n2
    real resultado
    logico aprovado = falso
    escreva("Digite a primeira nota: ")
    leia(n1)
    escreva("Digite a primeira nota: ")
    leia(n2)

    resultado = media(n1, n2)

    se (resultado >= 7 e resultado <= 13){
    aprovado = verdadeiro
    }
    senao{
      aprovado = falso
    }
    escreva("Média final: ", resultado)

    se (aprovado){
      escreva("\nAprovado")
    }

  }

}
