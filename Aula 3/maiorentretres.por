programa {
  funcao inicio() {
    real n1, n2, n3

    escreva("Digite o primeiro número: ")
    leia(n1)

    escreva("Digite o segundo número: ")
    leia(n2)

    escreva("Digite o terceiro número: ")
    leia(n3)

    se (n1 > n2 e n1 > n3 ){
      escreva("Primeiro número é maior!")
    } senao se (n2 > n1 e n2 >n3){
      escreva("Segundo número é maior!")
    } senao {
      escreva("Terceiro número é maior!")
    }
  }
}
