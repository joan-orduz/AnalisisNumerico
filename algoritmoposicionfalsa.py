import math

def posicion_falsa(f, a, b, eps, M):
    """
    Implementa el método de la Posición Falsa para encontrar una raíz de f(x)=0.
    """

    # Verificación del cambio de signo
    if f(a) * f(b) >= 0:
        print("Error: f(a) y f(b) no tienen signos opuestos")
        return

    print("\nMÉTODO DE LA POSICIÓN FALSA\n")

    # ===================== SECCIÓN DE RESULTADOS =====================
    print("=" * 80)
    print("RESULTADOS")
    print("=" * 80)

    # Explicación de las columnas
    print("\nEXPLICACIÓN DE LAS COLUMNAS:\n")
    print("n       = Número de iteración")
    print("a_n     = Extremo izquierdo del intervalo en la iteración n")
    print("b_n     = Extremo derecho del intervalo en la iteración n")
    print("f(a_n)  = Valor de la función evaluada en a_n")
    print("f(b_n)  = Valor de la función evaluada en b_n")
    print("x_n     = Nueva aproximación a la raíz (posición falsa)")
    print("f(x_n)  = Valor de la función evaluada en x_n\n")

    # Encabezado de la tabla
    print("{:<3} {:<10} {:<10} {:<12} {:<12} {:<12} {:<12}".format(
        "n", "a_n", "b_n", "f(a_n)", "f(b_n)", "x_n", "f(x_n)"
    ))
    print("-" * 85)

    # ===================== ITERACIÓN 0 =====================
    x_prev = (a * f(b) - b * f(a)) / (f(b) - f(a))

    print("{:<3} {:<10.6f} {:<10.6f} {:<12.6f} {:<12.6f} {:<12.6f} {:<12.6f}".format(
        0, a, b, f(a), f(b), x_prev, f(x_prev)
    ))

    # Actualización del intervalo
    if f(x_prev) * f(a) < 0:
        a_n, b_n = a, x_prev
    else:
        a_n, b_n = x_prev, b

    # ===================== ITERACIONES =====================
    for n in range(1, M + 1):

        x_n = (a_n * f(b_n) - b_n * f(a_n)) / (f(b_n) - f(a_n))
        error = abs((x_n - x_prev) / x_n)

        print("{:<3} {:<10.6f} {:<10.6f} {:<12.6f} {:<12.6f} {:<12.6f} {:<12.6f}".format(
            n, a_n, b_n, f(a_n), f(b_n), x_n, f(x_n)
        ))

        # Criterio de paro
        if error <= eps:
            print("\nÉXITO: se obtuvo una aproximación de la raíz")
            print(f"Raíz aproximada: {x_n}")
            print(f"Iteraciones realizadas: {n}")
            return

        # Actualización del intervalo
        if f(x_n) * f(a_n) < 0:
            b_n = x_n
        else:
            a_n = x_n

        x_prev = x_n

    # Fracaso
    print("\nFRACASO: después de M iteraciones no se logró la precisión deseada")


# ===================== PROGRAMA PRINCIPAL =====================

print("MÉTODO DE LA POSICIÓN FALSA\n")

# Entrada de datos
funcion = input("Ingrese la función f(x): ")
a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
eps = float(input("Ingrese la tolerancia ε: "))
M = int(input("Ingrese el número máximo de iteraciones: "))

# Definición de la función ingresada por el usuario
def f(x):
    return eval(funcion, {"x": x, "math": math})

# Ejecución del método
posicion_falsa(f, a, b, eps, M)