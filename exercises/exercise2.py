"""Lógica Simple y Cortocircuito"""


"""
Construir una expresión lógica que use TODAS las variables y cuyo resultado sea
True si al menos una de las variables es True.
"""

from operator import truediv


esta_lloviendo = True
riego_activado = True

# COMPLETAR - INICIO

piso_mojado=esta_lloviendo or riego_activado

# COMPLETAR - FIN

assert piso_mojado


"""
Construir una expresión lógica que use TODAS las variables y cuyo resultado sea
True si el área es mayor a 5.
Restricción: Usar NOT.
"""

lado_cuadrado = 5
area_cuadrado = pow(lado_cuadrado, 2)

# COMPLETAR - INICIO

area_mayor_a_cinco = area_cuadrado > 5 and not lado_cuadrado < 3

# COMPLETAR - FIN

assert area_mayor_a_cinco


"""
Construir una expresión lógica que use TODAS las variables y cuyo resultado sea
True si el número 1 es divisible por 7 y al mismo tiempo el número 2 no lo es.
"""

numero_1 = 49
numero_2 = 50

# COMPLETAR - INICIO

resultado = numero_1 % 7 == 0 and not numero_2 % 7 == 0

# COMPLETAR - FIN

assert resultado


"""
Construir una expresión lógica que use TODAS las variables y cuyo resultado sea
el mismo valor de la variable 3.
Restricción: sólo usar OR, NOT y el mecanismo de cortocircuito.
"""

variable_01 = False
variable_02 = True
variable_03 = 80
variable_04 = "90"
variable_05 = 100

# COMPLETAR - INICIO

resultado = variable_05 - 20 and variable_03 and variable_02 and not variable_01 and int(variable_04) - 10

# COMPLETAR - FIN

assert resultado == 80