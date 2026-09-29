programa {
  funcao desconto_progressivo(real preco){
    real desc
    se (preco >= 0 e preco < 100){
      desc = preco * 0.10
      preco = preco - desc
      escreva("Seu desconto é de 10%, o valor final é ", preco)
    }
    senao se (preco >= 100 e preco < 500){
      desc = preco * 0.15
      preco = preco - desc
      escreva("Seu desconto é de 15%, o valor final é ", preco)
    }
    senao se (preco >= 500){
      desc = preco * 0.20
      preco = preco - desc
      escreva("Seu desconto é de 20%, o valor final é ", preco)
    }
    senao{
      escreva("Valor inválido")
    }
  }
  funcao inicio() {
    real valor
    escreva("Digite o valor da compra e o programa verá o desconto que será aplicado: ")
    leia(valor)
    desconto_progressivo(valor)

  }
}
