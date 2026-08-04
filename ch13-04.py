#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 11:30:36 2026

@author: cristianramirez
"""

'''
Escribe un programa qque calcule la frecuencia de aparicion de cada letra en una cadena. Por ejemplo, para la cadena "abracadabra" debería mostrar: {'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}
'''
# Creamos el diccionario vacio
letras = {}

# Bucle para pedir al usuario la palabra que quiere comprobar
while True:
    palabra = input('Dime una palabra para contar las letras: ')
    # Condicion de salida para terminar el prograam
    if palabra.lower() == 'salir':
        break
    # Bucle para recorrer letra a letra la palabra indicada y almacenara en el diccionario para el conteo de letras.
    for letra in palabra:
        # Condicion de si la letra ya aparece en el diccionario sumamos +1 al contador de esa letra
        if letra in letras:
            letras[letra] += 1
        # Condicion de si la letra no aparece en el diccionario añadimos la letra como clave y inicamos contador en 1.
        else:
            letras[letra] = 1
            

print(letras)