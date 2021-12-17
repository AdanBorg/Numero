# -*- coding: utf-8 -*-
import os
os.system("clear")
def display():
   print('''
                d8b
                88P
               d88
 d888b8b   d888888   d888b8b    88bd88b
d8P' ?88  d8P' ?88  d8P' ?88    88P' ?8b
88b  ,88b 88b  ,88b 88b  ,88b  d88   88P
`?88P'`88b`?88P'`88b`?88P'`88bd88'   88b 

''')

display()

import phonenumbers
#colores
yellow='\033[93m'
gren='\033[92m'
cyan='\033[96m'
pink='\033[95m'
red='\033[91m'
white='\033[97m'
from phonenumbers import carrier, geocoder,timezone
print(pink + "¡hola!-- por favor ingresa el numero del cual quieres optener informacion-- Recuerda que tienes que poner el codigo del pais ejemplo +52(numero)")

mobileNo = input(red + "Ingresa el numero: ")
mobileNo = phonenumbers.parse(mobileNo)

#Sona del Orario
print(timezone.time_zones_for_number(mobileNo))

#coje la ubicacion
print(carrier.name_for_number(mobileNo,"en"))

#coje la rejion
print(geocoder.description_for_number(mobileNo,"en"))

#Validar numero
print("valido mobile numero: ",phonenumbers.is_valid_number(mobileNo))

#cheker de posibilidad validacion numero
print("chekando pacibilidad del  numero :",phonenumbers.is_possible_number(mobileNo))
