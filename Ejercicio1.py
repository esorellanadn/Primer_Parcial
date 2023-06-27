"""Escribe un programa que calcule la edad que cumplió o debe cumplir este año la persona, basado en el año de nacimiento."""

birthyear = int(input("Ingrese año de nacimiento: ")) #Ingreso de datos del usuario, Birth year significa año de nacimiento
actualyear = int(input("Ingrese año actual: ")) #Continua el ingreso de datos por parte del usuario, Actual year significa año actual
age = actualyear - birthyear #Luego llevo a cabo una resta con los datos que ingresó el usuario, Age significa edad

print ("Este año la persona deberia cumplir: ", age)