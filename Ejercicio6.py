"""Del punto anterior, calcular y mostrar por pantalla el sueldo bruto, el monto a bonificar y el sueldo neto (bruto+bonif)
a. Si trabajo más de 120hs por mes, la bonificación es de %18
b. Si trabajo entre 80 y 120hs, la bonificación es de %15
c. Si trabajo menos de 80hs, la bonificación es de %13"""

horas = int(input("Ingrese cuantas horas trabajó en el mes: ")) #Ingreso de datos
if horas > 120 and horas < 192: #De nuevo utilizo 192 horas como un limite natural
    sueldomes = horas * 1500
    bonif = sueldomes * 0.18 #Multiplico el sueldo mensual por 0.18 para obtener la bonificación
elif horas >= 80 and horas <= 120:
    sueldomes = horas * 1300
    bonif = sueldomes * 0.15 #Esta vez multiplico el sueldo mensual por 0.15
elif horas < 80: 
    sueldomes = horas * 1100
    bonif = sueldomes * 0.13 #Por ultimo multiplico el sueldo mensual por 0.13
elif horas > 192:
    print("El valor ingresado no es humanamente posible.")   

sueldoneto = sueldomes + bonif

print("Sueldo bruto: ", sueldomes)
print("Bonificación: ", bonif)
print("Sueldo neto: ", sueldoneto)