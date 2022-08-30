""""Tuplas y Desempaquetado"""


"""
A partir de ls siguiente lista instanciar una tupla que contenga todos sus valores
y en el mismo orden.
"""

lista = ["casa", "perro", "pato", "gato"]

# COMPLETAR - INICIO

tupla=(lista[0],lista[1],lista[2],lista[3])
print(tupla)


# COMPLETAR - FIN

assert tupla == ("casa", "perro", "pato", "gato")


"""
A partir de la siguiente tupla instanciar una lista que contenga todos sus valores
y en el mismo orden.
"""

tupla = "casa", "perro", "pato", "gato", "tenedor"

# COMPLETAR - INICIO

lista=[tupla[0],tupla[1],tupla[2],tupla[3],tupla[4]]

# COMPLETAR - FIN

assert lista == ["casa", "perro", "pato", "gato", "tenedor"]


"""
Desempaquetar la siguiente tupla en las variables a, b y c
"""

tupla = ("primer", 25, [1, 2, 3])

# COMPLETAR - INICIO

a,b,c=tupla

print(a,b,c)

# COMPLETAR - FIN

assert a == "primer" and b == 25 and c == [1, 2, 3]


"""
Desempaquetar la siguiente tupla y luego sumar sus valores
"""

tupla = (87, 98, 35, 67, 4, 9)

# COMPLETAR - INICIO

a,b,c,d,e,f=tupla
total=a+b+c+d+e+f
print(total)

# COMPLETAR - FIN

assert total == 300


"""
Desempaquetar la siguiente lista y luego concatenar sus elementos
Restricción: Utilizar f-Strings.
"""

lista = ["esta", "mañana", "sali", "a", "correr"]

# COMPLETAR - INICIO

a,b,c,d,e=lista
string_concatenado= f'{a} {b} {c} {d} {e}'
print(string_concatenado)
# COMPLETAR - FIN

assert string_concatenado == "esta mañana sali a correr"


"""
Desempaquetar el primer elemento de la siguiente tupla
Restricción: Utilizar desempaquetado con comodines
"""

tupla = (73, 45, 344, 3434, 2)

# COMPLETAR - INICIO

a,*rest=tupla
primer=a
print(primer)

# COMPLETAR - FIN

assert primer == 73


"""
Desempaquetar el primer y el último elemento de la siguiente lista y luego sumarlos
Restricción: Utilizar desempaquetado con comodines
"""

lista = [73, 45, 344, 3434, 2]

# COMPLETAR - INICIO

a,*rest,b=lista
suma=a+b
print(suma)

# COMPLETAR - FIN

assert suma == 75


"""
Desempaquetar el primer, el segundo, el tercer, el cuarto y el quinto elemento de la
siguiente tupla y luego concatenarlos
Restricción: Utilizar desempaquetado con comodines y f-Strings
"""

tupla = ("anoche", "fui", "a", "la", "fiesta", "pero", "no", "pude", "entrar")

# COMPLETAR - INICIO

a,b,c,d,e,*rest=tupla
string_concatenado=f'{a} {b} {c} {d} {e}'
print(string_concatenado)

# COMPLETAR - FIN

assert string_concatenado == "anoche fui a la fiesta"