"""Escribe un programa que calcule el promedio general de una clase."""

cont = 0 #Contador
sumanotas = 0 #Suma de todas las notas

alumnos = int(input("¿Cuantas notas desea ingresar?")) #El usuario ingresa la cantidad de notas de la clase

while cont < alumnos:
    nota = int(input("Ingrese la nota del estudiante: ")) #El usuario ingresa las notas una por una
    if nota > 10:
        print("Nota invalida.") #Si la nota tiene un valor mayor a 10 es invalida
    else:
        sumanotas += nota
        cont += 1
        
if cont > 0:
    prom = sumanotas / cont
    print("El promedio general de la clase es: ", prom) #Mostramos el promedio general