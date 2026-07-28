#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 19:06:47 2026

@author: cristianramirez
"""
'''
Escribe un programa que permita comprobar si las fechas de una lista son válidas o no. Para que una fecha sea válida deberá tener la estructura dd/mm/aa, es decir, dos dígitos para el día , dos para el mes y 4 para el año. Además, aaaa deberá se un valor comprendido entre 1900 y 2019.
'''

# Creo una lista con todas las fechas.
lista_fechas = ["25/12/2015", "1/1/20", "15/08/2026", "99/99/9999"]

# Bucle para recorrer todas las fechas.

for fecha in lista_fechas:
    dd_mm_aaaa = fecha.split("/") # Separo cada fecha como si fuera una lista.
    
    # Condicion para comprobar si la fecha es correcta comprobando cada una de las instrucciones.
    if len(dd_mm_aaaa[0]) == 2 and len(dd_mm_aaaa[1]) == 2 and len(dd_mm_aaaa[2]) == 4 and 1900 <= int(dd_mm_aaaa[2]) <= 2019:
        print(f'La fecha {fecha} es valida')
    
    else:
        print(f'La fecha {fecha} no es valida')
