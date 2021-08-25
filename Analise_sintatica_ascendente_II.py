def analisador(grammar, action, input, print_table = True):

  stack = []
  pos = 0
  
  if print_table:
    print("|{:>20}|{:>20}|".format("input", "stack"))
    print("|{}|{}|".format("-"*20, "-"*20))
    print("|{:>20}|{:>20}|".format(input[pos:], "".join([ str(s) for s in stack])))
  
  
  for i in range(len(action)):
    if actions[i] == "s":
      stack.append( input[pos])
      pos = pos + 1
    else:
      rule_index = action[i][1]
      rhs = grammar[rule_index][1]
      lhs = grammar[rule_index][0]
      
      for i in range(len(rhs)-1, -1, -1):
        
        if rhs[i] == stack[-1]:
          stack.pop()
        else:
          print("wrong parser")
      stack.append(lhs)
    if print_table:
      print("|{:>20}|{:>20}|".format(input[pos:], "".join([ str(s) for s in stack])))


grammar = [ 
      ("E", "E+T"  ), #rule 0           
      ("E",  "T"   ), #rule 1
      ("T",  "T*F" ), #rule 2           
      ("T",  "F"   ), #rule 3               
      ("F",  "(E)" ), #rule 4               
      ("F",  "a"   ), #rule 5               
]

input = "a*(a+a)$"

actions = [ "s", ("r", 5), ("r", 3), "s", "s", "s", ("r", 5), ("r", 3), ("r", 1), "s", "s", ("r", 5), ("r", 3), ("r", 0), "s", ("r", 4), ("r", 2), ("r", 1)]

analisador(grammar, actions, input )