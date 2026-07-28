#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 17:58:12 2026

@author: cristianramirez
"""

palabra = str(input('Escribe una palabra: '))
palabra = palabra.lower()

caracter_uno = palabra[0]
caracter_final = palabra[-1]

if caracter_uno == caracter_final:
    letras = 0
    for letra in palabra:
        if letra != caracter_uno:
            letras += 1
    print(letras)
    
else:
    palabra_recortada = palabra[1 : -1]
    letras = 0
    
    for letra in palabra_recortada:
        if letra == caracter_uno or letra == caracter_final:
            letras += 1
    print(letras)