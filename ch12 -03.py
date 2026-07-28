#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Las siguientes cadenas formateadas tienen errores. Realiza las correcciones necesarias para que sean válidas y pruebalas.
'''

# "No me canso de %s."%("aprender", "Python")

print("No me canso de %s. " %("aprender Python"))

# format("Estoy desdeando empezar el capítulo %d", 12)

print(("Estoy deseando empezar el capítulo {}"). format(12))

accion = 'formatear'
#f"Ya sé {s} cadenas en Python" % accion

print(f"Ya sé {accion} cadenas en Python")