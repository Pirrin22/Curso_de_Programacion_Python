#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 09:54:46 2026

@author: cristianramirez
"""

'''
Trabajas en el sistema informático de un concesionario. Tienes un texto donde los clientes han dejado comentarios, y necesitas extraer una lista limpia con todas las matrículas de coche españolas que mencionan.

Los formatos que tenemos que capturar son: AB1234AB, 1234ABC (sin espacios ni guiones). A los clientes a veces se les olvida y escriben las letras en minúsculas, así que tu programa debe atraparlas igual.
'''

import re

# Diccionario principal para almacenar los datos (clave: modelo, valor: matrícula)
registro_coches ={}

# ==========================================
# FASE 1: RECOPILACIÓN DE DATOS
# ==========================================

while True:
    # Solicitamos el modelo.
    modelo = input('Ingresa el Modelo del Vehiculo: ')
    
    # Condición de salida: convertimos a minusculas para aceptar "Salir", "SALIR", etc.
    if modelo.lower() == 'salir':
        break
    # Solicitamos la matrícula y la vinculamos a su modelo en el diccionario
    matricula = input('Ingresa la matricula del Vehiculo: ')
    registro_coches[modelo] = matricula
    
# ==========================================
# FASE 2: DEFINICIÓN DE PATRONES REGEX
# ==========================================
# Patrón 1: Matriculas modernas (Ej. 1234ABC) --> 4 números y 3 letras   
patron_1 = r'\b\d{4}[a-z]{3}\b'

# Patron 2: Provinciales antiguas (Ej. B1234AB o MA1234AB) --> 1 o 2 letras, 4 números, 2 letras
patron_2 = r'\b[a-z]{1,2}\d{4}[a-z]{2}\b'

# ==========================================
# FASE 3: FILTRADO Y MUESTRA DE RESULTADOS
# ==========================================

print('\n---Coches con matrículas válidas---')
    
# Recorremos cada par (modelo, matrícula) guardado en el diccionario
for modelo, matricula in registro_coches.items():
    
    # Comprobamos si la matrícula encaja con alguno de los 2 patrones.
    #La bandera re.I permite que acepte tanto mayúsculas como minúsculas.
    if re.search(patron_1, matricula, re.I) or re.search(patron_2, matricula, re.I):
        print(f'Modelo: {modelo} - Matricula: {matricula}')

