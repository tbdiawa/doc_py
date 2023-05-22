def additionner(val1,val2):
    return val1+val2

def multiplier(val1,val2):
    return val1*val2

def soustraire(val1,val2):
    return val1-val2

def diviser(val1,val2):
    return val1/val2

def puissance(val1,val2):
    return pow(val1,val2)
while True:             
    op=input("opérateur : ")
    if op== "+":
        val1=float(input("val1 : "))
        
        val2=float(input("val2 : "))
    
        resultat=additionner(val1,val2)
        print(val1,"+",val2,"=",resultat)
    elif op=="-":
        val1=float(input("val1 : "))
        
        val2=float(input("val2 : "))
    
        resultat=soustraire(val1,val2)
        print(val1,"-",val2,"=",resultat)
    elif op=="*":
        val1=float(input("val1 : "))
        
        val2=float(input("val2 : "))
    
        resultat=multiplier(val1,val2)
        print(val1,"*",val2,"=",resultat)

    elif op=="/":
        val1=float(input("val1 : "))
        
        val2=float(input("val2 : "))
        
        if val2!=0 :
            resultat=diviser(val1,val2)
            print(val1,"/",val2,"=",resultat) 
        else:
            print("division impossible ")    

    elif op=="^":
        val1=float(input("val1 : "))
        
        val2=float(input("val2 : "))
    
        resultat=puissance(val1,val2)
        print(val1,"^",val2,"=",resultat)  
    if op=="q":
        print("bye!")    
        break 
