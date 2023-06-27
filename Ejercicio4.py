"""En este ejercicio se debe indicar al usuario si aprobo o debe recursar su materia actual"""

nota1 = int(input("Ingrese la primer nota: ")) #Primero le pedimos al usuario la nota de su primer parcial
nota2 = int(input("Ingrese la segunda nota: ")) #Luego le pedimos al usuario que ingrese la nota de su segundo parcial
nota3 = int(input("Ingrese la tercer nota: ")) #Por ultimo el usuario debe ingresar la tercer nota de su tercer y ultimo parcial
prom = (nota1 + nota2 + nota3) / 3 

if prom > 6:
    print ("El alumno aprobó la materia.")
else:
    print ("El alumno recursa la materia.")