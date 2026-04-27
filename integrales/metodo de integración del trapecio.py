import math

def trapecio_compuesto(f, a, b, n):
    """
    Aproxima la integral de f en [a, b] usando la regla del trapecio compuesto.
    
    Parámetros:
        f : función a integrar
        a : límite inferior
        b : límite superior
        n : número de subintervalos
    
    Retorna:
        T(h) : aproximación de la integral
    """
    print("\nCalculando la integral usando el método del Trapecio compuesto...")
    print(f"Intervalo: [{a}, {b}]")
    print(f"Número de subintervalos (n): {n}")

    # Inicialización
    h = (b - a) / n          # Tamaño de cada subintervalo
    s0 = f(a) + f(b)         # Suma de los extremos
    s1 = 0                   # Acumulador de puntos interiores

    # Suma de los nodos interiores: i = 1, 2, ..., n-1
    for i in range(1, n):
        x = a + i * h
        s1 += f(x)

    # Fórmula del trapecio compuesto: T(h) = (h/2)*s0 + h*s1
    s = (h / 2) * s0 + h * s1

    return s


if __name__ == "__main__":

    print("=" * 60)
    print("     ALGORITMO DEL TRAPECIO COMPUESTO")
    print("=" * 60)

    # ----------------------------------------------------------------
    # Entrada 1: función f(x)
    # Se usa eval() para evaluar la expresión ingresada por el usuario.
    # Se prueba con x=0 y x=1 para detectar errores de sintaxis o de
    # dominio (ej: log de número negativo) antes de continuar.
    # ----------------------------------------------------------------
    print("\nIngrese la función a integrar en términos de x.")
    print("Puede usar: +, -, *, /, **, math.sin, math.cos, math.log, math.exp, etc.")

    while True:
        try:
            func_input = input("f(x) = ").strip()

            if not func_input:
                print("Error: La función no puede estar vacía. Intente nuevamente.")
                continue

            # Construimos la función usando eval con el módulo math disponible
            f = lambda x, expr=func_input: eval(expr, {"x": x, "math": math, "__builtins__": {}})

            # Prueba con dos valores para detectar problemas de dominio
            f(0)
            f(1)
            break

        except ZeroDivisionError:
            print("Advertencia: La función tiene una división por cero en x=0 o x=1.")
            print("Asegúrese de que f(x) esté definida en el intervalo que va a ingresar.")
            # Permitimos continuar: el error real se detectará al evaluar en [a, b]
            break
        except (NameError, SyntaxError) as e:
            print(f"Error de sintaxis en la función: {e}. Intente nuevamente.")
        except Exception as e:
            print(f"Error al evaluar la función: {e}. Intente nuevamente.")

    # ----------------------------------------------------------------
    # Entrada 2: extremos a y b del intervalo
    # Se valida que sean números reales y que a < b.
    # ----------------------------------------------------------------
    print("\nIngrese el intervalo de integración [a, b]:")

    while True:
        try:
            a = float(input("a = "))
            b = float(input("b = "))

            if math.isnan(a) or math.isnan(b):
                print("Error: Los límites están mal ingresados.")
            elif math.isinf(a) or math.isinf(b):
                print("Error: Los límites no pueden ser infinitos.")
            elif a >= b:
                print("Error: El límite inferior 'a' debe ser estrictamente menor que 'b'.")
            else:
                break

        except ValueError:
            print("Error: Ingrese valores numéricos válidos (use '.' como separador decimal).")

    # Verificamos que f esté definida en los extremos del intervalo real
    try:
        f(a)
        f(b)
    except Exception as e:
        print(f"\nAdvertencia: La función no pudo evaluarse en los extremos del intervalo: {e}")
        print("El cálculo puede fallar o producir resultados incorrectos.")

    # ----------------------------------------------------------------
    # Entrada 3: número de subintervalos n
    # Debe ser un entero positivo. A mayor n, mejor la aproximación.
    # ----------------------------------------------------------------
    print("\nIngrese el número de subintervalos (n entero positivo):")

    while True:
        try:
            n_input = input("n = ").strip()

            # Rechazamos explícitamente valores en punto flotante como "3.5"
            if '.' in n_input:
                print("Error: El número de subintervalos debe ser un entero, no un decimal.")
                continue

            n = int(n_input)

            if n <= 0:
                print("Error: El número de subintervalos debe ser un entero positivo (n ≥ 1).")
            else:
                break

        except ValueError:
            print("Error: Ingrese un número entero válido.")

    # ----------------------------------------------------------------
    # Cálculo y salida
    # ----------------------------------------------------------------
    try:
        resultado = trapecio_compuesto(f, a, b, n)
        print(f"\nT(h) ≈ {resultado}")
        print(f"      (con h = {(b - a) / n})")

    except ZeroDivisionError:
        print("\nError: División por cero al evaluar f(x) en algún nodo del intervalo.")
    except ValueError as e:
        print(f"\nError matemático al evaluar f(x): {e}")
        print("Verifique que la función esté definida en todo el intervalo [a, b].")
    except Exception as e:
        print(f"\nError inesperado durante el cálculo: {e}")