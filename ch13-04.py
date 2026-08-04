#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 11:30:36 2026

@author: cristianramirez
"""

'''
Escribe un programa qque calcule la frecuencia de aparicion de cada letra en una cadena. Por ejemplo, para la cadena "abracadabra" debería mostrar: {'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}
'''
letras = {}
palabra = ''

while True:
    palabra = input('Dime una palabra para contar las letras: ')
    
    if palabra.lower() == 'salir':
        break
    
    for letra in palabra:
        if letra in letras:
            letras[letra] += 1
        else:
            letras[letra] = 1
    print(letras)