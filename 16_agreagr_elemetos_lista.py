#solo se pueden concatenar listas con listas
#maneras de agragar elementos a listas
A = [1,2,3,4,5]

m1 = A + [1]
print(m1)

m2 = A + ['ABC']
print(m2)

m3 = A + list('ABC')
print(m3)

m4 = A + list(str(123))
print(m4)

m5 = A + [[6,7,8]]
print(m5)

m6 = A.append([6,7,8]) #devuelve una lista vacia
print(m6)