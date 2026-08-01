#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 10:00:51 2026

@author: cristianramirez
"""

'''
Escribe una expresión regular que permita extraer todas las palabras que terminen en os o as o sus equivalentes en mayúscula usando banderas.
'''
import re

frase = 'En mis casas tenemos tres Gatos los cuales se llaman Eustaquio, Elusipito y carmela. Los gatos son escurridizos y unos artistas para hacer travesuras'

patron = re.findall(r'\w+[oa]s\b', frase, re.I)


print(patron)