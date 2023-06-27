"""Escribe un programa solicite y muestre por pantalla el nombre, apellido y edad de 5 personas."""

cont = 1
while cont <= 5: #Coloqué un limite de 5 "Sujetos"
    print("Sujeto", cont) 
    nombre = input("Ingrese un nombre: ") #Ingreso de datos del sujeto o persona
    apellido = input("Ingrese un apellido: ") #Continua el ingreso de datos por parte del usuario
    edad = int(input("Ingrese una edad: ")) #Finaliza el ingreso de datos, coloqué la variable edad como númerica 
    print("Nombre: ", nombre)
    print("Apellido: ", apellido)
    print("Edad: ", edad)

    cont += 1 #Incrementa el valor de "Sujeto" por uno despues de ingresar todos los datos