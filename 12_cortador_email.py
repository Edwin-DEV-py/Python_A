#obtener email
email = str(input("Cual es tu correo?:")).strip() #eliminamos los espacios

#cortar nombre de usuario
x = email[:email.index("@")]

#cortar dominio
y = email[email.index("@")+1:]

#formatear le mensaje
mensaje = f'estes es tu nombre= {x} y este tu dominio= {y}'

#mostrar el mensaje
print(mensaje)