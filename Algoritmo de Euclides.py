# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 10:48:27 2021

Nombre: Gustavo Reyes Herrera
RUT: oculto

Mis respuestas en este trabajo son propias, y están realizadas
en conformidad con la formación ética de la universidad.

"""

# Función que calculará el máximo común divisor entre dos números entregados por el usuario


def euclides(n, x):  # Parametros 'n' y 'x'
    if n > x:  # Si n es mayor a x
        a = n
        b = x
    else:  # Si x es mayor a n
        a = x
        b = n
    while b != 0:  # Mientras b sea distinto de 0
        c = a % b
        a = b
        b = c
    return a


numN = int(input("Ingrese el primer valor: "))
numX = int(input("Ingrese el segundo valor: "))

resultado = euclides(numN, numX)

print(f"El máximo común divisor entre {numN} y {numX} es {resultado}")
