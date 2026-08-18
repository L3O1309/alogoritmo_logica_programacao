programa {
  funcao inicio() {
    real idade
    escreva("Digite sua idade: ")
    leia(idade)

    se (idade >= 16 e idade < 18 ){
      escreva("Pode votar, mas não é obrigatório!")
    } senao se (idade >= 18){
      escreva("Pode votar!")
    } senao {
      escreva("Não pode votar")
    }
  }
}
