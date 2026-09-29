programa {
  funcao forma_pagamento(inteiro opcao){
    escolha(opcao){
    caso 1: 
      escreva("Opção 1: Débito")
      pare
    caso 2:
      escreva("Opção 2: Crédito")
      pare
    caso 3:
      escreva("Opção 3: Parcelado 3x sem juros")
      pare
    caso 4:
      escreva("Opção 4: Parcelado 6x com juros")
      pare
    caso contrario:
      escreva("Opção inválida!")
    }
  }
  funcao inicio() {
    inteiro option
    escreva("Você possui 4 formas de pagamento, digite 1-4 para escolher a forma do pagamento: ")
    leia(option)
    forma_pagamento(option)
    
  }
}
