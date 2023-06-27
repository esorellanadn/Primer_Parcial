"""Escribe un programa que solicite y muestre por pantalla nombre, apellido y edad de una cantidad de personas ingresadas por el usuario."""

personas = int(input("¿Cuantas personas desea ingresar?: "))

cont = 1
while cont <= personas: #Número de personas ingresadas por el usuario
    print("Sujeto", cont) 
    nombre = input("Ingrese un nombre: ") #Ingreso de datos del sujeto o persona
    apellido = input("Ingrese un apellido: ") #Continua el ingreso de datos por parte del usuario
    edad = int(input("Ingrese una edad: ")) #Finaliza el ingreso de datos, coloqué la variable edad como númerica 
    print("Nombre: ", nombre)
    print("Apellido: ", apellido)
    print("Edad: ", edad)

    cont += 1