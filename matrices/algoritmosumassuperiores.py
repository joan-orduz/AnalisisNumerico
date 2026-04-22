import math

# -------- FUNCIÓN PARA CREAR LA FUNCIÓN DESDE EL TEXTO --------
def crear_funcion(expresion):
    def f(x):
        return eval(expresion, {"x": x, "math": math})
    return f


# -------- FUNCIÓN SUMA SUPERIOR CON PROCESO --------
def suma_superior_con_proceso(f, a, b, n):
    delta_x = (b - a) / n
    s = 0

    print("\n" + "=" * 60)
    print("           PROCESO DE LA SUMA SUPERIOR U(A)")
    print("=" * 60)
    print(f"Intervalo: [{a}, {b}]")
    print(f"Número de subintervalos: {n}")
    print(f"Delta x = (b - a)/n = ({b} - {a})/{n} = {delta_x}")
    print("-" * 60)

    for i in range(1, n + 1):
        x_anterior = a + (i - 1) * delta_x
        x_actual = a + i * delta_x

        fx_anterior = f(x_anterior)
        fx_actual = f(x_actual)

        fx_sup = max(fx_anterior, fx_actual)
        area_rectangulo = fx_sup * delta_x
        s += area_rectangulo

        print(f"\nSubintervalo {i}: [{x_anterior}, {x_actual}]")
        print(f"f({x_anterior}) = {fx_anterior}")
        print(f"f({x_actual}) = {fx_actual}")
        print(f"Máximo = max({fx_anterior}, {fx_actual}) = {fx_sup}")
        print(f"Área del rectángulo {i} = {fx_sup} * {delta_x} = {area_rectangulo}")
        print(f"Suma acumulada = {s}")

    print("\n" + "-" * 60)
    print(f"Resultado final: U(A) = {s}")
    print("=" * 60)

    return s


# -------- PROGRAMA PRINCIPAL --------
try:
    # Validar función
    while True:
        expresion = input("Ingrese la función en términos de x (ej: x**2, math.sin(x)): ")
        try:
            f = crear_funcion(expresion)
            prueba = f(1)
            break
        except Exception:
            print(" Error: la función no es válida. Intente de nuevo.")

    # Validar a
    while True:
        try:
            a = float(input("Ingrese el valor de a: "))
            break
        except ValueError:
            print(" Error: debe ingresar un número válido para a.")

    # Validar b
    while True:
        try:
            b = float(input("Ingrese el valor de b: "))
            if b <= a:
                print(" Error: b debe ser mayor que a.")
            else:
                break
        except ValueError:
            print(" Error: debe ingresar un número válido para b.")

    # Validar n
    while True:
        try:
            n = int(input("Ingrese el número de subintervalos n: "))
            if n <= 0:
                print(" Error: n debe ser un entero positivo.")
            else:
                break
        except ValueError:
            print(" Error: debe ingresar un número entero válido para n.")

    # Calcular mostrando el proceso
    suma_superior_con_proceso(f, a, b, n)

except Exception as e:
    print(" Ocurrió un error inesperado:", e)