programa {
  funcao inicio() {
    escreva("BOLETIM DE NOTAS")
    
  //Strings
    cadeia nome
    cadeia disciplina
    cadeia curso
    inteiro semestre
    real nota1
    real nota2
    real notafinal

  //Dados
    escreva("\nNome do(a) aluno(a): ")
    leia(nome)
  
    escreva("\nNome do curso: ")
    leia(curso)

    escreva("\nNome da disciplina: ")
    leia(disciplina)

    escreva("\nQual semestre está: ")
    leia(semestre)

    escreva("\nNota do primeiro bimestre da disciplina: ")
    leia(nota1)

    escreva("\nNota do segundo bimestre da disciplina: ")
    leia(nota2)

    notafinal = (nota1 + nota2) / 2 

  //Saídas
    escreva("\nNome: ", nome)
    escreva("\nCurso: ", curso)
    escreva("\nDisciplina: ", disciplina)
    escreva("\nSemestre: ", semestre)
    escreva("\nMédia: ", notafinal)

  //Statu do aluno
    se (notafinal >= 60 e notafinal < 101){
      escreva("\nEstá aprovado")
    } senao se (notafinal > 39 e notafinal < 60){
      escreva("\nEstá de recuperação")
    } senao se (notafinal > 0 e notafinal < 40 ){
      escreva("\nEstá reprovado")
    } senao {
      escreva("\nTente novamente, algo deu errado!")

  }
  }
}
