# encoding: iso-8859-1
# Todo nao terminal será representado por uma letra maiúscula
# Todo terminal será representado por uma letra minúsculas
# O conjunto de regras é representado por uma lista de pares ordenado


def check_derivation(grammar, sentencial_form, derivation, string):
  print("rightmost derivation ", string)  
  print(sentencial_form)
  
  for i in range(len(derivation)):
    rule_index = derivation[i]    
    found = False    
    for pos in range( len(sentencial_form)-1, -1, -1 ):      
      symbol = sentencial_form[pos]
      if symbol == grammar[rule_index][0]:
        sentencial_form = sentencial_form[0:pos] + grammar[rule_index][1] + sentencial_form[pos+1:]
        found = True
        break
    
    if not found:
      print ("wrong derivation")
      return 

    print ("=>", sentencial_form)        
  
  if sentencial_form == string:
    print ("complete derivation")
  else:
    print ("wrong derivation") 




 
#Considere a seguinte gramatica
grammar2 = [ 
      ("E", "E+T"  ), #rule 0           
      ("E",  "T"   ), #rule 1
      ("T",  "T*F" ), #rule 2           
      ("T",  "F"   ), #rule 3               
      ("F",  "(E)" ), #rule 4               
      ("F",  "a"   ), #rule 5               
]

# Construa uma derivacao mais à direita para as seguintes palavras: 
# Coloque aqui sua derivacao mais à direita

X = [0, 3, 5, 1, 2, 5, 3, 5]
check_derivation(grammar2, "E", X, "a*a+a")

X = [1, 2, 4, 0, 3, 5, 1, 3, 5, 3, 5]
check_derivation(grammar2, "E", X, "a*(a+a)")