"""Escribe un programa que muestre los números del 1 al 10. Además, el programa debe mostrar:
a. Si el número es par o impar.
b. Cuanto es la suma total de todos los números mostrados.
c. Cuanto es la suma total de todos los números pares mostrados.
d. Cuanto es la suma total de todos los números impares mostrados."""

num = 1
sumanums = 0 #Suma de todos los números mostrados
sumapar = 0 #Suma de todos los números pares
sumaimpar = 0 #Suma de todos los números impares

while num <= 10:
    print(num)
    sumanums += num
    if num %2 == 0:
        print("El número es par.")
        sumapar += num
    else:
        print("El número es impar")
        sumaimpar += num
    num += 1

print("La suma de todos los números es: ", sumanums)  
print("La suma de todos los números pares es: ", sumapar)   
print("La suma de todos los números impares es: ", sumaimpar)