from typing import NamedTuple
import sys
import re

Token = NamedTuple('Token', [('type', str), ('value', str), ('line', int), ('column', int)])
    
     
def tokenize(code):
    # palavras-chaves da linguagem analisada
    keywords = {'IF', 'THEN', 'ENDIF', 'FOR', 'NEXT', 'GOSUB', 'RETURN'}
    # lista com o identificador do token e a expressão regular que descreve o token    
    token_specification = [
        # Observe que a especificação do token NUMBER aceita números inteiros e decimais
        # Os números decimais descritos a parte inteira é obrigatória 
        ('NUMBER',   r'\d+(\.\d*)?'),  # Integer or decimal number
        ('ASSIGN',   r'='),           # Assignment operator
        ('AP', r'[(]'),
        ('AC', r'[{]'),
        ('COMMA', r'[,]'),
        ('LEFTBRACKET', r'[[]'),
        ('RIGHTBRACKET', r'[]]'),
        ('for', r'for'),
        ('LT', r'[<]'),
        ('FP', r'[)]'),
        ('FC', r'[}]'),
        ('if', r'if'),
        ('return', r'return'),
        ('END',      r';'),            # Statement terminator
        ('ID',       r'[A-Za-z]+'),    # Identifiers
        ('OP',       r'[+\-*/]'),      # Arithmetic operators
        ('NEWLINE',  r'\n'),           # Line endings
        ('SKIP',     r'[ \t]+'),       # Skip over spaces and tabs
        #('MISMATCH', r'.'),            # Any other character
    ]
    
    # Com esse comando construímos uma expressão regular com todos os tokens da linguagem
    # Por exemplo,
    # tok_regex = (?P<NUMBER>\d+(\.\d*)|(?P<ID>[A-Za-z]+))
    # É uma expressão regular que descreve os tokens NUMBER e ID


    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
    line_num = 1
    line_start = 0
    # A função finditer(tok_regex, code) devolve um iterador de match objects
    # Os atributos e métodos de match object mo utilizados são: 
    # * mo.lastgroup devolve o nome do último match capturado
    # * mo.group() devolve o último match encontrado
    # * mo.start() devolve o indice do inicio da substring casada pelo group
    

    for mo in re.finditer(tok_regex, code):
        kind = mo.lastgroup
        value = mo.group()
        column = mo.start() - line_start
        if kind == 'NUMBER':
            value = str(value) if '.' in value else str(value)
        elif kind == 'ID' and value in keywords:
            kind = value
        elif kind == 'NEWLINE':
            # Cada vez que o caractere \n é encontrado o numero de linhas é incrementado            
            line_start = mo.end()
            line_num += 1
            continue
        elif kind == 'SKIP':
            continue
        yield Token(kind, value, line_num, column)

data = sys.stdin.readlines(200)

code = ''.join(data)

for token in tokenize(code):
    print(token)

"""
A análise léxica pode ser realizada utilizando expressões regulares para descrição dos tokens. Considere o seguinte trecho de código:

    IF quantity THEN
        total := total + price * quantity;
        tax := price * 0.05;
    ENDIF;
A análise léxica vai “quebrar” o código em tokens. No relatório abaixo, vamos listar os tokens encontrados no código acima. Cada token tem um tipo, um valor associado, a linha e a coluna que ele aparece. Por exemplo, o código acima obteremos o seguinte relatório:

Token(type='IF', value='IF', line=1, column=4)
Token(type='ID', value='quantity', line=1, column=7)
Token(type='THEN', value='THEN', line=1, column=16)
Token(type='ID', value='total', line=2, column=8)
Token(type='ASSIGN', value=':=', line=2, column=14)
Token(type='ID', value='total', line=2, column=17)
Token(type='OP', value='+', line=2, column=23)
Token(type='ID', value='price', line=2, column=25)
Token(type='OP', value='*', line=2, column=31)
Token(type='ID', value='quantity', line=2, column=33)
Token(type='END', value=';', line=2, column=41)
Token(type='ID', value='tax', line=3, column=8)
Token(type='ASSIGN', value=':=', line=3, column=12)
Token(type='ID', value='price', line=3, column=15)
Token(type='OP', value='*', line=3, column=21)
Token(type='NUMBER', value=0.05, line=3, column=23)
Token(type='END', value=';', line=3, column=27)
Token(type='ENDIF', value='ENDIF', line=4, column=4)
Token(type='END', value=';', line=4, column=9)

Observe que cada lexema da linguagem está classificado em um token. Observe também que podemos ter vários lexemas associado a um mesmo tipo de token.


Entrada

if(quantity){ 
  total = total + price * quantity; 
}
Saída

Token(type='if', value='if', line=1, column=0)
Token(type='AP', value='(', line=1, column=2)
Token(type='ID', value='quantity', line=1, column=3)
Token(type='FP', value=')', line=1, column=11)
Token(type='AC', value='{', line=1, column=12)
Token(type='ID', value='total', line=2, column=2)
Token(type='ASSIGN', value='=', line=2, column=8)
Token(type='ID', value='total', line=2, column=10)
Token(type='OP', value='+', line=2, column=16)
Token(type='ID', value='price', line=2, column=18)
Token(type='OP', value='*', line=2, column=24)
Token(type='ID', value='quantity', line=2, column=26)
Token(type='END', value=';', line=2, column=34)
Token(type='FC', value='}', line=3, column=0)

Entrada

int main(){
  int a, b, c;
  int v[10];
  s = 0;  
  for(int i = 0; i < n; i = i + 1){
    s = s + i
  }  

  
  if (quantity) { 
    total = total + price * quantity + 34 + 1.23; 
  }
  return 0;
}
Saída

Token(type='ID', value='int', line=2, column=0)
Token(type='ID', value='main', line=2, column=4)
Token(type='AP', value='(', line=2, column=8)
Token(type='FP', value=')', line=2, column=9)
Token(type='AC', value='{', line=2, column=10)
Token(type='ID', value='int', line=3, column=2)
Token(type='ID', value='a', line=3, column=6)
Token(type='COMMA', value=',', line=3, column=7)
Token(type='ID', value='b', line=3, column=9)
Token(type='COMMA', value=',', line=3, column=10)
Token(type='ID', value='c', line=3, column=12)
Token(type='END', value=';', line=3, column=13)
Token(type='ID', value='int', line=4, column=2)
Token(type='ID', value='v', line=4, column=6)
Token(type='LEFTBRACKET', value='[', line=4, column=7)
Token(type='NUMBER', value='10', line=4, column=8)
Token(type='RIGHTBRACKET', value=']', line=4, column=10)
Token(type='END', value=';', line=4, column=11)
Token(type='ID', value='s', line=5, column=2)
Token(type='ASSIGN', value='=', line=5, column=4)
Token(type='NUMBER', value='0', line=5, column=6)
Token(type='END', value=';', line=5, column=7)
Token(type='for', value='for', line=6, column=2)
Token(type='AP', value='(', line=6, column=5)
Token(type='ID', value='int', line=6, column=6)
Token(type='ID', value='i', line=6, column=10)
Token(type='ASSIGN', value='=', line=6, column=12)
Token(type='NUMBER', value='0', line=6, column=14)
Token(type='END', value=';', line=6, column=15)
Token(type='ID', value='i', line=6, column=17)
Token(type='LT', value='<', line=6, column=19)
Token(type='ID', value='n', line=6, column=21)
Token(type='END', value=';', line=6, column=22)
Token(type='ID', value='i', line=6, column=24)
Token(type='ASSIGN', value='=', line=6, column=26)
Token(type='ID', value='i', line=6, column=28)
Token(type='OP', value='+', line=6, column=30)
Token(type='NUMBER', value='1', line=6, column=32)
Token(type='FP', value=')', line=6, column=33)
Token(type='AC', value='{', line=6, column=34)
Token(type='ID', value='s', line=7, column=4)
Token(type='ASSIGN', value='=', line=7, column=6)
Token(type='ID', value='s', line=7, column=8)
Token(type='OP', value='+', line=7, column=10)
Token(type='ID', value='i', line=7, column=12)
Token(type='FC', value='}', line=8, column=2)
Token(type='if', value='if', line=11, column=2)
Token(type='AP', value='(', line=11, column=5)
Token(type='ID', value='quantity', line=11, column=6)
Token(type='FP', value=')', line=11, column=14)
Token(type='AC', value='{', line=11, column=16)
Token(type='ID', value='total', line=12, column=4)
Token(type='ASSIGN', value='=', line=12, column=10)
Token(type='ID', value='total', line=12, column=12)
Token(type='OP', value='+', line=12, column=18)
Token(type='ID', value='price', line=12, column=20)
Token(type='OP', value='*', line=12, column=26)
Token(type='ID', value='quantity', line=12, column=28)
Token(type='OP', value='+', line=12, column=37)
Token(type='NUMBER', value='34', line=12, column=39)
Token(type='OP', value='+', line=12, column=42)
Token(type='NUMBER', value='1.23', line=12, column=44)
Token(type='END', value=';', line=12, column=48)
Token(type='FC', value='}', line=13, column=2)
Token(type='return', value='return', line=14, column=2)
Token(type='NUMBER', value='0', line=14, column=9)
Token(type='END', value=';', line=14, column=10)
Token(type='FC', value='}', line=15, column=0)

"""

