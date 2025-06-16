"""
    Gestión de excepciones

"""

try:            # Para capturar excepciones.
    código 1    # Código a ejecutar.

except:
    código 2    # Se ejecuta si se produce error en código 1.



finally:        # Opcional.
    código 3    # Se ejecuta siempre aunque haya error en código 1.


raise ValueError()  # Generar un error.
