for i in range(1, 11):
    if i == 5:
        break
    print(i, end=" ")
print()
print("_______________________________________________")
for i in range(1, 11):
    if i == 5:
        continue
    print(i, end=" ")
print()
print("_______________________________________________")
for i in range(0,20):
    print(i, end=" ")
print()
print("_______________________________________________")
from math import sin
for x in range(-3, 4): 
    try:
        print("{:.3f}".format(sin(x)/x), end=" , ")
    except:
        print("{:.3f}".format(float(1)), end=" , ")
print()
print("_______________________________________________")
def table(base, debut, fin, inc):
    n = debut
    while n <= fin:
        print(n, 'x', base, '=', n*base)
        n = n + inc
table(7, 2, 13, 1)
print("_______________________________________________")

nombres = [17, 38, 10, 25, 72]
print(" Liste initiale ".center(50, '-'))
print(nombres, '\n')
rien = input('"Entree"')
print(" Tri ".center(50, '-'))
nombres.sort()
print(nombres, '\n')
rien = input('"Entree"')
print(" Ajout d'un element ".center(50, '-'))
nombres.append(12)
print(nombres, '\n')
rien = input('"Entree"')
print(" Retournement ".center(50, '-'))
nombres.reverse()
print(nombres, '\n')
rien = input('"Entree"')
print(" Indice d'un element ".center(50, '-'))
print(nombres.index(17), '\n')
rien = input('"Entree"')
print(" Retrait d'un element ".center(50, '-'))
nombres.remove(38)
print(nombres, '\n')
rien = input('"Entree"')
print(" Indicage ".center(50, '-'))
print("nombres[1:3] =", nombres[1:3])
print("nombres[:2] =", nombres[:2])
print("nombres[2:] =", nombres[2:])
print("nombres[:] =", nombres[:])
print("nombres[-1] =", nombres[-1])
print("_______________________________________________")

truc = []
machin = [0.0]*5
print("truc =", truc)
print("machin =", machin, "\n")
rien = input('"Entree"')
print("range(4) =", range(4))
print("range(4, 8) =", range(4, 8))
print("range(2, 9, 2) =", range(2, 9, 2), "\n")
rien = input('"Entree"')
chose = range(6)
print("chose =", chose)
rien = input('"Entree"')
print("Test d'appartenance de l'element 3 :", 3 in chose)
print("Test d'appartenance de l'element 6 :", 6 in chose)

print("_______________________________________________")

result1 = []
for i in range(6):
    result1.append(i+3)
print(" boucle for ".center(50, '-'))
print(result1, '\n')
rien = input('"Entree"')
result2 = [i+3 for i in range(6)]
print(" forme 1 ".center(50, '-'))
print(result2)
