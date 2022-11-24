#####For
#diferente linea
for contador in range(1,10):
    print(contador)
#en una sola linea
for contador in range(1,10):
    print(contador,end=" ")
    
#iterar 1
frutas = {'Fresa':'roja', 'Limon':'verde', 'Papaya':'naranja'}
for fruta,color in frutas.items():
    print(fruta, "es de color", color)
    
#iterar 2
for fruta1 in frutas:
    print(fruta1, "es de color", frutas[fruta1])
    
######while
