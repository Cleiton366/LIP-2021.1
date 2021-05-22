import re

def find_float(code):
    pattern = r'[-+][0-9.][.0-9]+|[0-9.][.0-9]+'
    codeList = code.split()
    for i in codeList:
        if(re.fullmatch(pattern, i)):
            print(i)

code = input()
find_float(code)        

"""
Faça um programa que recebe um código de um programa e devolve todas as constante ponto flutuante contidas no seu programa.

Uma constante ponto-flutuante consiste em uma palavra com:

Um sinal de + ou - opcional
Uma string de dígitos
Um ponto decimal
Uma outra string de dígitos. Essa outra string de dígitos ou a primeira string de dígitos (2) podem ser vazias, mas não ambas.
Entrada

int main(){ float a = 3 ; float b = .2 ; float c = 1. ; float d = 5.9 ; float e = -2. ; float f = +3.6 ; float g = . ; }
Saída

.2
1.
5.9
-2.
+3.6

"""