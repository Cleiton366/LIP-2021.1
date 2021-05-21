def counting_lexemes(code, lexeme):
  codeList = code.split()
  res = 0
  for i in codeList:
    if(i.find(lexeme) != -1):
        res += 1  
  print (res)


code = input()
lexeme = input()
counting_lexemes(code, lexeme)


"""
Durante o processo de análise léxica, o código-fonte do programa é lido e separado em palavras que chamamos lexemas. Em seguida, esses lexemas são classificados em tokens. Essa sequência de tokens é enviada para ser analisada pela análise sintática.

Considere o seguinte código:

int main(){
  int a1, a2;
  a1 = a1 + 2;
  a2 = a1 + 5;  
}
O lexema a1 é classificado como um id.

A sua tarefa é dada um código-fonte encontre quantas vezes um dado lexema aparece no código.

Use a função find(sub, [ start [, end]]) que retorna o índice mais baixo na string onde a substring sub é encontrado dentro da fatia s[start:end]. Argumentos opcionais como start e end são interpretados como na notação de fatiamento. Retorna -1 se sub não for localizado.
"""