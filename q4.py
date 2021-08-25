import re

code = input()

## Coloque aqui usa expressão regular
pattern = r'[+-]?([0-9]+\.([0-9]*)?|[.][0-9]+)'

for s in code.split():
  if re.fullmatch(pattern, s) :
    print(s) 