"""Escribe un programa que calcule la equivalencia a pesos de los dólares ingresados por pantalla. El programa debe preguntar el tipo de cambio a convertir (es decir, cuánto cotiza el dólar)"""

dollar = int(input("Ingrese cantidad de dólares a convertir: ")) #El usuario ingresa cuantos dólares desea convertir
valuedollar = int(input("Ingrese valor del dólar: ")) #Le pido al usuario que ingrese el valor del dólar ya que varia constantemente, valluedollar significa valor del dolar
pesoar = dollar * valuedollar #Multiplico el dolar por el valor del dolar para obtener la equivalencia en pesos

print ("El equivalente en pesos seria: ", pesoar)