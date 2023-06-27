"""Escribe un programa que permita ingresar las edades de las personas, hasta que el usuario decida no
hacerlo más, y muestre, al final, un promedio de las edades ingresadas y el total de personas ingresadas."""

cont = 0 #Contador.
acum = 0 #Acumulador.
con = 1  #Booleano.
while con == 1:
    edad = int(input("Ingrese una edad: ")) #Ingreso de datos por parte del usuario.
    cont += 1 
    acum = acum + edad
    con = int(input("Si desea seguir ingresando edades presione 1 sino presione 0. ")) #Le pregunto al usuario si desea seguir ingresando mas edades.
    prom = acum / cont #Calculo el promedio dividiendo los valores acumulados por los valores contados.
    if con == 0: 
        print("El promedio de las edades ingresadas es de", prom)
        print("Total de personas ingresadas:", cont)
    elif con > 1:
        print("El valor ingresado es incorrecto.") #El valor de "con" no debe superar el 1.