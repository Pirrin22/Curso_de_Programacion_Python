#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 10:31:03 2026

@author: cristianramirez
"""
# Cadena a modificar.
frase = "Mi nombre es Paula"
# Separamos la cadena en subcadenas, cada palabra sera una cadena.
palabras = frase.split()
# Cambiamos el ultimo item por la palabra que queremos
palabras[-1] = 'Cristian'
# Juntamos de nuevo la cadena con el metodo .join()
frase = ' '.join(palabras)
# Imprimimos cadena completa con el cambio hecho.
print(frase)
