import re


## Coloque aqui usa expressão regular
#regexp = r'[xX][0-9a-fA-F]+'

regexp = r'(?:0[xX])?[0-9a-fA-F]+'

for string in input().split(' '):
  print( re.fullmatch(regexp, string) != None)