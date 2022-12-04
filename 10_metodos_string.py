#contar letras de una palabra o texto
print("hola".count("o"))
texto = "hola, como estas?"
print(texto.count("o"))
print(texto.count("hola"))

#pasar de mayusculas a minusculas y al reves
x = "Hola Maria"
print(x.lower())
print(x.upper())

#primera letra mayuscula
print(x.capitalize())

#preguntar 
print(x.islower())

#metodos
print(x.title()) # cada palabra comienza con mayuscula
print(x.istitle())

#verificar que tipo es
#isalpha para letras sin espacios
#isdigit para numeros
#isalnum para valors combinados

#buscar letras o palabras
print(x.index("M"))
print(x.find("M"))

#eliminar letras
print(x.strip("H"))
print(x.lstrip("Hola"))
print(x.rstrip("a"))

#contar letras
print(len(x))