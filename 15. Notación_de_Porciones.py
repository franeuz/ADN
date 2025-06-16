"""
    Notación por porciones

Para listas, tuplas, cadenas de texto y otras secuencias.

"""

# porciones desde ini hasta fin
# tomando elementos de paso

sec[ini:fin:paso]

sec = [10, 20, 30, 40, 50, 60]


sec[2:5] == [30, 40, 50] 

sec[4:] == [50, 60]

sec[:2] == [10, 20]

sec[1:6:2] == [20, 40, 60]

sec[4:1:-1] == [50, 40, 30]

sec[:] == [10, 20, 30, 40, 50, 60]

sec[::-1] == [60, 50, 40, 30, 20, 10]




