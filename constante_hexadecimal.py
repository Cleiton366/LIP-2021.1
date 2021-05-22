import re

def hexadecimal(code):
    pattern = r'0[xX][0-9a-fA-F]+'
    codeList = code.split()
    for i in codeList:
        print(re.fullmatch(pattern, i) != None)

code = input()
hexadecimal(code)


"""
Faça um programa que lê uma linha formada por várias strings e verifica se cada uma das strings corresponde
a constante hexadecimal. Um constante hexadecimal começa com 0, seguido de x ou X,
seguido dos dígitos de 0 até 9 ou os caracteres de a até f, maiúsculos ou minúsculos.

Entrada

0x23 0xFF 0x2F 0xG5 0xFF 0XA0000024
Saída

True
True
True
False
True
True
"""