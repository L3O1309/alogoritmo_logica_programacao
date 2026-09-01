programa {
  funcao inicio() {

    escreva("ESTÁ CHOVENDO! \n")

    logico chovendo = falso

    escreva("\nEstá chovendo agora? (sim/não): ")
    leia(chovendo)

    se (nao(chovendo))
    {
      escreva ("\nNão está chovendo!")
    }
    senao
    {
      escreva ("\nEstá chovendo!")
    }
  }
}
