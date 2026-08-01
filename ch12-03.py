#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 10:42:31 2026

@author: cristianramirez
"""

'''
Escribe un programa para remplazar por 'X' los números de teléfono de los clientes de una compañía que aparezcan en un texto. Los números de teléfono de los clientes tienen el formato xxx-xxx-xxx(ej.640-321-895)
'''
import re
texto = 'El cliente Antonio con telefono 654-090-469 y la clienta Eustaquia con telefono 649-456-972 tienen un premio por fidelidad.'
texto_clave = 'X'

patron = r'\d{3}-\d{3}-\d{3}'

telefono_encriptado = re.sub(patron, texto_clave, texto)

print(telefono_encriptado)