"""Ejercicio 1:
Escriba el programa correspondiente en lenguaje Python de los siguientes algoritmos:
a) Mostrar el mensaje "Hola Mundo".
b) Ingresar el nombre del usuario del programa y saludarlo.
c) Ingresar dos números y mostrar la suma y la diferencia.
d) Ingresar tres números y mostrar la suma y el promedio.
e) Ingresar el monto de una factura y calcular el IVA (21%).
"""

print("Hola Mundo")

nombre = input("Ingrese su nombre:")

print("Bienvenido ",nombre)

numeroUno = int(input("Ingrese un número:"))
numeroDos = int(input("Ingrese un segundo número:"))
numeroTres = int(input("Ingrese un tercer número:"))

suma = numeroUno + numeroDos + numeroTres

resta = numeroUno - numeroDos - numeroTres

print("La suma de los numeros es: ",suma)
print("La resta de los numeros es: ",resta)

promedio = float(suma/3)

print("El promedio de los 3 números es: ", promedio)

montoFactura = float(input("Ingrese el monto de la factura:"))

iva = montoFactura * 0.21

montoFinal = montoFactura + iva

print("El monto ingresado es: ", montoFactura)
print("El monto del IVA es: ", iva)
print("El valor total a pagar + iva es: ", montoFinal)