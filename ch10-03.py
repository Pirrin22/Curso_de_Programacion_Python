#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 12:13:12 2026

@author: cristianramirez
"""

lluvia_mensual = [65, 70, 87, 62, 44, 14, 5, 5, 24, 50, 57, 69]
meses = ['Enero',  'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']

max_lluvia = max(lluvia_mensual)# Calcula aquí el máximo valor de lluvia registrada
mes_max = lluvia_mensual.index(max_lluvia) # Obtén el índice del mes correspondiente
print(f'El mes más lluvioso a sido {meses[mes_max]} con {max_lluvia} litros')