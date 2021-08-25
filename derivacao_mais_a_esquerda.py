
def check_derivation(grammar, sentencial_form, derivation, string):
  print (sentencial_form)
  
  for i in range(len(derivation)):
    rule_index = derivation[i]    
    found = False    
    for pos in range( len(sentencial_form) ):      
      symbol = sentencial_form[pos]
      if symbol == grammar[rule_index][0]:
        sentencial_form = sentencial_form[0:pos] + grammar[rule_index][1] + sentencial_form[pos+1:]
        found = True
        break
    
    if not found:
      print ("derivacao mal formada")
      return 

    print ("=>" + sentencial_form)        
  
  if sentencial_form == string:
    print ("derivacao completa")
  else:
    print ("derivacao imcompleta")


grammar2 = [ 
      ("E", "E+T"  ), #rule 0           
      ("E",  "T"   ), #rule 1
      ("T",  "T*F" ), #rule 2           
      ("T",  "F"   ), #rule 3               
      ("F",  "(E)" ), #rule 4               
      ("F",  "a"   ), #rule 5               
]

# Construa uma derivacao para a + a + a
# Coloque aqui sua derivacao

X = [0, 0, 1, 3, 5, 3, 5, 3, 5]
check_derivation(grammar2, "E", X, "a+a+a")

#X = [0, 1, 3, 2, 3, 5, 5, 5]
X = [0, 1, 3, 5, 2, 3, 5, 5]
check_derivation(grammar2, "E", X, "a+a*a")
