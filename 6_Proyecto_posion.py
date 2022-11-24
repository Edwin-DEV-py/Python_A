import random

salud=50
dificultad = 2
posion = int(random.randint(25,50) / dificultad)
salud = salud+posion #reescribimos sobre la variable salud, le damos un nuevo valor
print(salud)