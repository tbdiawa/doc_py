pren=["alexandre","amandine","anna"];
print (pren);
print(pren[0]);
print(pren[2]);
pren[2]="hannah";
print(pren);
pren.insert(3,"yvette");
print(pren);
pren.insert(1,"alexis");
print(pren);
print(pren[1:2]);
print(pren[-1]);
print(pren[0:2]);
pren[0:2]=["paul","jacques"];
print(pren);
print(len(pren));
print(pren[4]);
print(pren[-1]);
print(pren[-3]);
pren.append("eléonore");
print(pren);
pren.extend(["audrey","ophélie"]);
print(pren);
del pren[1:3];
print(pren);
pren.pop(4);
print(pren);
pren.remove("paul");
print(pren);
pren.clear();
print(pren);

print("_______________________________________________")

gar=["alexandre","alexis"];
fil=["delphine","zoe"];
prenom=(gar,fil);
print(gar);
print(fil);
print(prenom);
print(prenom[1]);
print(prenom[1][0]);
print(prenom[1][0][2]);

print("_______________________________________________")
n=str(input("sessie le 1er prenom : "));
o=str(input("sessie le 2é prenom : "));
p=str(input("sessie le 3é prenom : "));
m=str(input("sessie le 4é prenom : "));
t=str(input("sessie le 5é prenom : "));
liste=[n,o,p,m,t];
print(liste);
print(type(n));
print(type(liste));

print("_______________________________________________")
a=[1,2,5,9,8];
print(a);

print("_______________________________________________")
b=10;
print(b<12);
print(type(b));
print(b==4);
print(b!=2);
print(b//4);

print("_______________________________________________")
r="TATA";
r2=r.lower();
print(r);
print(r2);

print("_______________________________________________")
chaine=input("Note sur 20 : ");
note=float(chaine);
if note>20 or note<0:
    print("Note invalide!");
else:
    if note>=10.00:
        print("j'ai la moyenne");
    if note==20:
        print("C'est même excellent");
    else:
        if note<=10.00:
            print("C'est en dessous de la moyenne");
print("fin de programme");