import math

def posicion_falsa(f, a, b, eps, M):
    """
    Implementa el método de la Posición Falsa para encontrar una raíz de f(x)=0.

    Parámetros:
    f   : función a la que se le busca la raíz
    a,b : extremos del intervalo inicial [a,b] con f(a)*f(b) < 0
    eps : tolerancia (error máximo permitido)
    M   : número máximo de iteraciones
    """

    # Verificación del cambio de signo en el intervalo inicial
    if f(a) * f(b) >= 0:
        print("Error: f(a) y f(b) no tienen signos opuestos")
        return

    # Encabezado de la tabla
    print("\nMétodo de la Posición Falsa\n")
    print("{:<3} {:<10} {:<10} {:<12} {:<12} {:<12} {:<12}".format(
        "n", "a_n", "b_n", "f(a_n)", "f(b_n)", "x_n", "f(x_n)"
    ))
    print("-" * 85)

    # ---------------- ITERACIÓN 0 ----------------
    # Cálculo inicial de x0 usando la fórmula de la posición falsa
    x_prev = (a * f(b) - b * f(a)) / (f(b) - f(a))

    # Se imprime la fila n = 0
    print("{:<3} {:<10.6f} {:<10.6f} {:<12.6f} {:<12.6f} {:<12.6f} {:<12.6f}".format(
        0, a, b, f(a), f(b), x_prev, f(x_prev)
    ))

    # Actualización del intervalo según el signo de f(x0)
    if f(x_prev) * f(a) < 0:
        a_n, b_n = a, x_prev
    else:
        a_n, b_n = x_prev, b

    # ---------------- ITERACIONES ----------------
    for n in range(1, M + 1):

        # Cálculo de xn
        x_n = (a_n * f(b_n) - b_n * f(a_n)) / (f(b_n) - f(a_n))

        # Cálculo del error relativo
        error = abs((x_n - x_prev) / x_n)

        # Se imprime la fila correspondiente a la iteración n
        print("{:<3} {:<10.6f} {:<10.6f} {:<12.6f} {:<12.6f} {:<12.6f} {:<12.6f}".format(
            n, a_n, b_n, f(a_n), f(b_n), x_n, f(x_n)
        ))

        # Criterio de paro: si el error es menor o igual a la tolerancia
        if error <= eps:
            print("\nÉXITO: se obtuvo una aproximación de la raíz")
            print(f"Raíz aproximada: {x_n}")
            print(f"Iteraciones realizadas: {n}")
            return

        # Actualización del intervalo [a_n, b_n]
        if f(x_n) * f(a_n) < 0:
            b_n = x_n
        else:
            a_n = x_n

        # Se guarda xn como valor anterior para la siguiente iteración
        x_prev = x_n

    # Si se llega al máximo de iteraciones sin cumplir la tolerancia
    print("\nFRACASO: después de M iteraciones no se logró la precisión deseada")


# ================= PROGRAMA PRINCIPAL =================

print("MÉTODO DE LA POSICIÓN FALSA\n")

# Entrada de datos por teclado
funcion = input("Ingrese la función f(x): ")
a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
eps = float(input("Ingrese la tolerancia ε: "))
M = int(input("Ingrese el número máximo de iteraciones: "))

# Definición de la función f(x) a partir de la entrada del usuario
def f(x):
    return eval(funcion, {"x": x, "math": math})

# Llamada al método
posicion_falsa(f, a, b, eps, M)