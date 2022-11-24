#Simple: comparar dos valores
a=1
b=2
if a>b:
    print("Opcion1")
if b>a:
    print("Opcion2")
if b!=a:
    print("Opcion3")
if b==a:
    print("Opcion4")

#Medio: anadiendo Else
if a>b:
    print("a es mayor que b")
else:
    print("b es mayor que a")

#AND y OR
if b>a and b!=a:
    print(True)
    
if b>a or b==a:
    print(True)
    
#if anidado
c = 3
if b>a:
    if c>b:
        print(True)
else:
    print(False)