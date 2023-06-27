"""Del punto anterior, y considerando que durante 12 meses el empleado trabajó las mismas cantidades de
horas, escribe un programa que calcule el descuento anual a realizarse, considerando:
a. Si el sueldo anual es mayor a $2.000.000, el descuento es del %5.
b. Si el sueldo anual esta entre $1.000.000 y $2.000.000, debe aplicarse un descuento del %3.
c. Si el sueldo anual es menor a $1.000.000, debe aplicarse un descuento del %1.
d. El programa debe mostrar el salario anual bruto, el monto anual de bonificaciones, el monto anual
a descontarse y las horas trabajadas en todo el año."""

horas = int(input("Ingrese cuantas horas trabajó en el mes: ")) #Ingreso de datos
if horas > 120 and horas < 192: #Como en los programas anteriores pongo de limite 192 horas
    sueldomes = horas * 1500
    bonificacion = sueldomes * 0.18 #Multiplico el sueldo mensual por 0.18 para obtener la bonificación
elif horas >= 80 and horas <= 120:
    sueldomes = horas * 1300
    bonificacion = sueldomes * 0.15 #Esta vez multiplico el sueldo mensual por 0.15
elif horas < 80: 
    sueldomes = horas * 1100
    bonificacion = sueldomes * 0.13 #Por ultimo multiplico el sueldo mensual por 0.13, hasta este punto mantengo los mismos comentarios que en el programa anterior
elif horas > 192:
    print("El valor ingresado no es humanamente posible.")  

sueldoneto = sueldomes + bonificacion #Multiplico el sueldo mensual por la bonificacion para obtener el sueldo neto

print("Sueldo bruto: ", sueldomes) 
print("Bonificación: ", bonificacion)
print("Sueldo neto: ", sueldoneto)

sueldoanual= sueldomes * 12 #Multiplico el sueldo mensual por 12 para obtener el sueldo anual
trabajoanual= horas * 12 #Utilizo el mismo proceso para obtener las horas trabajadas durante el año
bonifanual= bonificacion * 12 #Y por ultimo lo hago con la bonificación mensual para obtener la bonificación anual

if sueldoanual > 2000000:
    descuento = sueldoanual * 0.05

elif sueldoanual >= 1000000 and sueldoanual <= 2000000:
    descuento = sueldoanual * 0.03

elif sueldoanual > 1000000:
    descuento = sueldoanual * 0.01

print("Salario bruto: ", sueldoanual)
print("Bonificación: " , bonifanual)
print("Monto a descontarse: ", descuento) 
print("Horas trabajadas durante el año: ", trabajoanual)
