import math
a=0;
while(a<7):
    a=a+1;
    print(a, end=" ");
print()

print("_______________________________________________")
a=int(input("entrez la valeur : "));
if(a%2==0):
    print("a est pair");
else:
    print("a est impair");

d=int(input("Entrez d : "));
if d>0:
    print("d est positif");
elif d<0:
    print("d est negatif");
else:
    print("d est nul");

print("_______________________________________________")

a=int(input("valeur de a : "));
b=int(input("valeur de b : "));
c=int(input("valeur de c : "));
x1=int;
x2=int;
delta=int;
if a==0:
    print("Equation du 1er degré");
    x1=-c/b;
    print(x1);
else:
    if a+b+c==0:
        x1=1;
        x2=c/a
        print(x1);
        print(x2);
    else:
        if a+c==b:
            x1=-1;
            x2=-c/a;
            print(x1);
            print(x2);
        else:
            delta=(b*b)-(4*a*c);
            if delta<0:
                print("pas de solution");
            else :
                if delta==0:
                    print("Solution double!");
                    x1=x2=-b/(2*a);
                    print(x1);
                    print(x2);
                else:
                    x1=(-b-math.sqrt(delta))/(2*a);
                    x2=(-b+math.sqrt(delta))/(2*a);
                    print(x1);
                    print(x2);
