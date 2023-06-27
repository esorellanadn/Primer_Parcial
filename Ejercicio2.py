"""Escribe un programa que calcule el área y el perimetro de un cuadrado y muestre los resultados (Indicando cuál es cuál) por pantalla"""

lado = int(input("Ingrese el lado de un cuadrado: ")) #El usuario ingresa el lado de un cuadrado
area = lado * lado #Multiplico lado por lado para obtener el area
perim = lado * 4 #Multiplico lado por cuatro para obtener el perimetro

print ("El area del cuadrado es: ", area)
print ("El perimetro del cuadrado es: ", perim)