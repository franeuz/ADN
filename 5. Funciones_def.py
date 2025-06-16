"""
   Funciones  -->  def funcion(parámetro):
                       print(f"Hola, {nombre}!")  # Cuerpo de la función
                       return suma(a, b)          #La función puede devolver un valor al código que la llamó mediante la palabra clave return.                        

Se inicia con la palabra clave def, seguida del nombre de la función y, opcionalmente, parámetros entre paréntesis. 
Dos puntos (:):

Después de la definición de la función, se agregan dos puntos para indicar el inicio del cuerpo de la función. 

Cuerpo de la función: El cuerpo es un bloque de código que se ejecuta cuando la función es llamada. Puede contener: 

Declaraciones: Declaración de variables, asignaciones, etc.

Instrucciones: Sentencias que realizan operaciones (imprimir, calcular, llamar a otras funciones, etc.). 
Sentencias de control: if, elif, else, for, while, break, continue, pass. 

Llamadas a otras funciones: La función puede llamar a otras funciones para realizar tareas específicas. 

Indización: El cuerpo de la función debe estar sangrado (identado) para indicar que pertenece a la definición de la función. En Python, la sangría es obligatoria y se suele usar 4 espacios para cada nivel de sangría. 

Return (opcional): La función puede devolver un valor al código que la llamó mediante la palabra clave return. 

"""

def suma(a,b):
    return a+b
r = suma(10,15)     # r == 25


print(r)


def opera(a,b,c):
    return suma(a,b), b-c
r, s = opera(10,15,3) # r == 25
                      # s == 12

print("r :", r, "\ns :", s)

