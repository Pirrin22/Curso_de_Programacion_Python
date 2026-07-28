# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import datetime

def edad(anio_nac):
    """
    Esta función calcula los años que cumples en el año actual
    """
    hoy = datetime.datetime.today()
    return hoy.year - anio_nac

mi_edad = edad(1992)

# mostramos el resultado en pantalla
print(f'Este año cumples {mi_edad} años')