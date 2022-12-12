usuarios = ["Nicolas","Maria","Edwin","Angel"]
print(len(usuarios))

while True:
    print("Hola")
    nombre = str(input("cual es tu nombre?:")).strip().capitalize()
    if nombre in usuarios:
        print("Bienvenido "+nombre)
        eliminar = input("Quieres ser eliminado del sistema (y/n)?:").lower()
        if eliminar == "y":
            usuarios.remove(nombre)
            print("Usuario eliminado", usuarios)
        else:print("No hay problema, hasta pronto")
    else:
        print("Nombre no reconocido")
        agregar = input("Te gustaria ser registrado (y/n)?:").lower()
        if agregar == "y":
            usuarios.append(nombre)
            print(f'{nombre} has sido anadido al sistema')
            print(usuarios)
        else:print("No hay problema, hasta pronto")
    
    break