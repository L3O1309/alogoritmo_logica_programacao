programa {
  funcao inicio() {
    real n 
    escreva("Digite um número: ")
    leia(n)

    se (n > 0){
      escreva("Número positivo")
    } senao se (n < 0){
      escreva("Número negativo")
    } senao {
      escreva("Igual a zero")
    }

  }
}
