def E():
    print("Entrando E")
    print("E -> TE'")    
    T()
    E_()
    print("Saindo E")
    

def E_():
    global pos
    global proxCaractere
    global error
    print("Entrando E'")
    if proxCaractere == '+':
        print("E' -> +TE'")        
        pos = pos + 1
        proxCaractere = s[pos]
        T()
        E_()
    elif proxCaractere not in ['$', ')', "*"]:
        error = True
        print("erro sintatico")
    else:
        print("E' -> ''")        
        
    print("Saindo E'")

#T -> FT'
def T():
    print("Entrando T")
    print("T -> FT'")        
    F()
    T_()
    print("Saindo T")
    
#T' ->*FT'

def T_():
    global pos
    global proxCaractere
    global error
    print("Entrando T'")
    
    if proxCaractere == ")":
        pos = pos + 1
        proxCaractere = s[pos]
        print("T' -> ''")

    elif proxCaractere == '*':
        print("T' -> *FT'")
        pos = pos + 1
        proxCaractere = s[pos]
        F()
        T_()
    elif proxCaractere not in ['$', '+', ')']:
        error = True
        print("erro sintatico")
    else:
        print("T' -> ''")
            
    print("Saindo T'")
def F():
    global pos
    global proxCaractere
    global error 
    print("Entrando F")
    
    
    if proxCaractere == 'a':
        print("F -> a")
        pos = pos + 1
        proxCaractere = s[pos]
    elif proxCaractere == "(":
         print("F -> (E)")
         pos = pos + 1
         proxCaractere = s[pos]
         E()
    else:
        error = True
        print("erro sintatico")
    print("Saindo F")
    
s = input()
pos = 0
proxCaractere = s[pos]
error = False

E()

if proxCaractere == '$' and not error:
    print("string aceita")
else: 
    print("erro sintatico")