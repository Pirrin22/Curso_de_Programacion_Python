#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 10:36:06 2026

@author: cristianramirez
"""

'''
El siguiente programa lee valores del teclado para crear una colección de contactos
bajo la forma de lista de diccionarios. Solo cuando se introducen valores no vacíos, se almacenan en el diccionario

El número total de contactos esindefinido y depende del usuario, el que se le pregunta si desea introducir más contactos después de cada uno de ellos

- Primera funcionalidad: Aumentar el programa con el codigo necesario para calcular y mostrar el número total de contactos almacenados y cuántos de ellos deisponen de correo electronico.

- Segunda funcionalidad: Una vez introducidos los datos, ¿Que código de una sola línea serviría para asignar al primer contacto los mismos valores asociados al último.

- Tercera funcionalidad: Escribe el código para mostata los datos del usuario cuyo correo electrónico haya sido introducido por teclado. Si no existe contacto alguno con ese correo electrónico, se mostrará el mensaje << No encontrado >>.
'''

# Datos a solicitar para cada contacto
campos = ('nombre', 'apellidos', 'email', 'teléfono')

# esta lista contendrá todos los contactos
contactos = []

# Iniciamos la variable 'seguir'
seguir = 's'

# mientras el valor de seguir sea 's' o 'S' introducimos contactos
while seguir in('s', 'S'):
    
    # Este diccionario almacena los valores de un contacto
    contacto = {}
    
    # Con este bucle preguntamos campo a campo
    for campo in campos:
        valor = input(campo + ': ')
        
        # Si el usuario introduce algo, se almacena
        if len(valor) > 0:
            contacto[campo] = valor
    
    # Añadimos el contacto a la lista
    contactos.append(contacto)
    
    # Preguntamos si seguimos añadiendo contactos
    seguir = input('¿Introducir otro contacto? s/n: ')
    
# Contador de los contactos con email
con_email = 0
  
# Mostramos todos los contactos
for contacto in contactos:
    
    # Comprobamos si el contacto tiene email asignado o no
    if 'email' in contacto:
        con_email += 1
    for k,v in contacto.items():
        print(f'{k} -> {v}')
        
    # Mostramos esto para facilitar lectura
    print('--------')
    
# Preguntamos al usuario que email quiere buscar.   
email_buscar = input('¿Que email quieres buscar: ')

# Variable chivato
encontrado = False

for contacto in contactos:
    if 'email' in contacto and contacto['email'] == email_buscar:
        encontrado = True
        # Bucle para imprimir los datos de Este contacto   
        for k,v in contacto.items():
            print(f'{k} -> {v}')
        
if encontrado == False:
    print('No encontrado')


# Copiamos el valor del ultimo contacto al primer contacto
contactos[0] = contactos[-1].copy()

# Mostramos el total de contactos en el diccionario   
print(f'Número total de contactos: {len(contactos)}')

# Mostramos el total de contactos con email en el diccionario
print(f'Número de contactos con email: {con_email}')