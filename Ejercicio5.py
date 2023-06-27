"""Escribe un programa que calcule el sueldo de un empleado basándose en la cantidad de horas y muestre por pantalla el resultado, considerando lo siguiente:
a. Si trabajo más de 120hs por mes, la hora tiene un valor de $1500.
b. Si trabajo entre 80 y 120hs por mes, la hora tiene un valor de $1300.
c. Si trabajo menos de 80hs por mes, la hora tiene un valor de $1100"""

horas = int(input("Ingrese cuantas horas trabajó en el mes: ")) #Ingreso de datos, en este caso horas trabajadas al mes
if horas > 120 and horas < 192: #El 192 representa el máximo de horas que un ser humano puede trabajar al mes
    sueldomes = horas * 1500 #Si el usuario trabaja más de 120 horas con un limite 192 horas multiplico las horas por 1500

elif horas >= 80 and horas <= 120: 
    sueldomes = horas * 1300 #Si el usuario trabaja entre 80 hasta 120 multiplico las horas por 1300
elif horas < 80: 
    sueldomes = horas*1100 #Si el usuario trabaja menosde 80 horas multiplico las horas por 1100
    
print ("Tu sueldo es segun tu horas trabajadas son: ", sueldomes ,"pesos")