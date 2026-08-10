programa {
  funcao inicio() {
    escreva("BOLETIM DE NOTAS")
    
    //Strings
    cadeia nome
    cadeia disciplina
    real nota

    //Dados
    escreva("\nNome do(a) aluno(a): ")
    leia(nome)

  escreva("\nNome da disciplina: ")
  leia(disciplina)

  escreva("\nNota da disciplina: ")
  leia(nota)

  se (nota >= 60 e nota < 101){
    escreva("\nEstá aprovado")
  } senao se (nota > 39 e nota < 60){
    escreva("\nEstá de recuperação")
  } senao se (nota > 0 e nota < 40 ){
    escreva("\nEstá reprovado")
  } senao {
    escreva("\nNúmero inválido")

  }
  }
}
