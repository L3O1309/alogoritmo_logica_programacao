programa {
  funcao inicio() {
    
    escreva ("PRÁTICA ESPORTIVA + AUTORIZAÇÃO! \n")
    
    inteiro idade
    logico autorizacao

    escreva("\nEscreva sua idade: ")
    leia (idade)
    escreva("Você tem autorização?(sim/não): ")
    leia(autorizacao)

    se (idade >= 12 e idade <= 18 e autorizacao == verdadeiro)
    {
      escreva ("\nVocê pode participar da prática!")
    }
    senao
    {
      escreva("\nVocê não pode participar da prática!")
    }
  }
}
