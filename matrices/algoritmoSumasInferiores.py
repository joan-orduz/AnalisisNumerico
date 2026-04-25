"""
Pseudocodigo:
-------------------------------------------------------------
Entrada:
  - f(x)  : funcion
  - a, b  : intervalo
  - n     : numero de subintervalos (entero positivo)

Salida:
  - L(A)  : Area inferior aproximada

Pasos:
  1. Se define:
       Delta_x = (b - a) / n
       x_i = a + i * Delta_x    para i en {0, 1, ..., n}

  2. Sea S = 0
     Para i = 1(1)n, haga:
       Sea f(x_i) = min{ f(x_{i-1}), f(x_i) }
       S = S + f(x_i)

  Salida: L(A) = Delta_x * S
-------------------------------------------------------------

Valores aceptados para a y b:
  Enteros    ->  3   -2   0
  Decimales  ->  1.5  -0.75
  Fracciones ->  3/4  -1/2  1/3

Funciones disponibles:
  sin, cos, tan, exp, log, log2, log10, sqrt, pi, e, abs
  Ejemplos: x**2   x**3 - 2*x   sin(x)   sqrt(x)   exp(x)
"""

import math
from fractions import Fraction


# ==============================================================
# PARSEO Y FORMATO
# ==============================================================

def parsear_numero(texto):
    """
    Convierte string a float via Fraction para soportar fracciones exactas.
    Acepta : 3  -2  1.5  -0.75  3/4  -1/2  1/3
    Rechaza: letras, notacion cientifica, denominador 0
    """
    texto = texto.strip()
    if not texto:
        raise ValueError("El valor esta vacio.")
    for c in texto:
        if c.isalpha():
            raise ValueError(
                f"'{texto}' contiene letras. Solo se aceptan numeros "
                f"(ej: 3, -1, 1.5, 3/4)."
            )
    try:
        valor = float(Fraction(texto))
    except ZeroDivisionError:
        raise ValueError(f"'{texto}': el denominador no puede ser 0.")
    except Exception:
        raise ValueError(
            f"'{texto}' no es un numero valido. "
            f"Use enteros (3, -1), decimales (1.5) o fracciones (3/4)."
        )
    return valor


ENTORNO_FUNCIONES = {
    "sin":   math.sin,
    "cos":   math.cos,
    "tan":   math.tan,
    "exp":   math.exp,
    "log":   math.log,
    "log2":  math.log2,
    "log10": math.log10,
    "sqrt":  math.sqrt,
    "pi":    math.pi,
    "e":     math.e,
    "abs":   abs,
}


def construir_funcion(expr):
    """
    Construye una funcion evaluable a partir de una expresion string.
    Lanza ValueError si la expresion no es valida con x = 1.
    """
    try:
        entorno = dict(ENTORNO_FUNCIONES)
        entorno["x"] = 1.0
        eval(expr, {"__builtins__": {}}, entorno)
    except Exception as e:
        raise ValueError(
            f"La expresion '{expr}' no es valida: {e}\n"
            f"  Use solo x y las funciones listadas arriba."
        )

    def f(x, _expr=expr):
        entorno = dict(ENTORNO_FUNCIONES)
        entorno["x"] = x
        return eval(_expr, {"__builtins__": {}}, entorno)

    return f


# ==============================================================
# FUNCIONES DE ENTRADA
# ==============================================================

def leer_funcion():
    """Solicita y valida una funcion matematica en terminos de x."""
    while True:
        try:
            expr = input("  f(x) = ").strip()
            if not expr:
                print("  No ingreso nada. Ingrese una expresion valida (ej: x**2).")
                continue
            f = construir_funcion(expr)
            return f, expr
        except ValueError as e:
            print(f"  {e}")
        except KeyboardInterrupt:
            print("\n\n  Interrumpido. Saliendo...")
            raise


def leer_numero(mensaje, nombre):
    """Solicita y valida un numero real o fraccion."""
    while True:
        try:
            entrada = input(mensaje).strip()
            if not entrada:
                print(f"  No ingreso nada. Ingrese un valor para {nombre}.")
                continue
            valor = parsear_numero(entrada)
            return valor, entrada
        except ValueError as e:
            print(f"  {e}")
        except KeyboardInterrupt:
            print("\n\n  Interrumpido. Saliendo...")
            raise


def leer_entero_positivo(mensaje):
    """Solicita y valida un entero positivo para n."""
    while True:
        try:
            entrada = input(mensaje).strip()
            if not entrada:
                print("  No ingreso nada. Ingrese un entero positivo (ej: 4).")
                continue
            if "." in entrada:
                print(f"  '{entrada}' es decimal. n debe ser un entero positivo.")
                continue
            for c in entrada.replace("-", ""):
                if c.isalpha():
                    print(f"  '{entrada}' contiene letras. Ingrese solo digitos.")
                    break
            else:
                n = int(entrada)
                if n <= 0:
                    print(f"  '{n}' debe ser mayor que 0.")
                else:
                    return n
        except ValueError:
            print("  Valor no reconocido. Ingrese un entero positivo (ej: 4).")
        except KeyboardInterrupt:
            print("\n\n  Interrumpido. Saliendo...")
            raise


# ==============================================================
# ALGORITMO: SUMAS INFERIORES
# ==============================================================

def sumas_inferiores(f, a, b, n):
    """
    Calcula la Suma de Riemann Inferior L(A) de f en [a, b]
    con n subintervalos, siguiendo el pseudocodigo del algoritmo.

    Retorna:
      L       : valor de la suma inferior
      tabla   : lista de dicts con los valores de cada paso
      delta_x : ancho de cada subintervalo
      S       : suma acumulada de los minimos
    """
    # Paso 1: definir Delta_x
    delta_x = (b - a) / n

    # Paso 2: Sea S = 0
    S = 0.0
    tabla = []

    for i in range(1, n + 1):
        x_prev = a + (i - 1) * delta_x   # x_{i-1}
        x_curr = a + i * delta_x          # x_i

        f_prev = f(x_prev)
        f_curr = f(x_curr)

        # f(x_i) = min{ f(x_{i-1}), f(x_i) }
        f_min = min(f_prev, f_curr)

        # S = S + f(x_i)
        S += f_min

        tabla.append({
            "i":      i,
            "x_prev": x_prev,
            "x_curr": x_curr,
            "f_prev": f_prev,
            "f_curr": f_curr,
            "f_min":  f_min,
        })

    # Salida: L(A) = Delta_x * S
    L = delta_x * S
    return L, tabla, delta_x, S


# ==============================================================
# IMPRESION DE RESULTADOS
# ==============================================================

def imprimir_tabla(tabla, delta_x, S, L):
    """
    Imprime la tabla de resultados paso a paso,
    consistente con la tabla del pseudocodigo.
    """
    ancho = 78

    encabezado = (
        f"  {'i':>3}  "
        f"{'x(i-1)':>11}  "
        f"{'x(i)':>11}  "
        f"{'f(x(i-1))':>12}  "
        f"{'f(x(i))':>12}  "
        f"{'min':>12}"
    )

    print()
    print("=" * ancho)
    print(f"  {'TABLA DE RESULTADOS  -  SUMAS INFERIORES':^{ancho - 2}}")
    print("=" * ancho)
    print(encabezado)
    print("-" * ancho)

    for fila in tabla:
        print(
            f"  {fila['i']:>3}  "
            f"{fila['x_prev']:>11.6f}  "
            f"{fila['x_curr']:>11.6f}  "
            f"{fila['f_prev']:>12.6f}  "
            f"{fila['f_curr']:>12.6f}  "
            f"{fila['f_min']:>12.6f}"
        )

    print("-" * ancho)
    print(f"  {'Suma  S = sum f(x_i)':>{ancho - 16}} {S:>12.6f}")
    print(f"  {'Delta_x = (b - a) / n':>{ancho - 16}} {delta_x:>12.6f}")
    print("=" * ancho)
    print(f"  L(A) = Delta_x * S  =  {delta_x:.6f} * {S:.6f}  =  {L:.6f}")
    print("=" * ancho)


# ==============================================================
# PROGRAMA PRINCIPAL
# ==============================================================

def main():
    print("=" * 62)
    print("  TAREA 1 - ALGORITMO DE SUMAS INFERIORES")
    print("  Calculo de la Suma de Riemann Inferior L(A)")
    print("=" * 62)
    print("  Valores aceptados para a y b:")
    print("    Enteros    ->  3  -2  0")
    print("    Decimales  ->  1.5  -0.75")
    print("    Fracciones ->  3/4  -1/2  1/3")
    print()
    print("  Funciones disponibles en f(x):")
    print("    sin, cos, tan, exp, log, log2, log10, sqrt, pi, e, abs")
    print("    Ejemplos:  x**2   x**3 - 2*x   sin(x)   sqrt(x)")
    print()

    seguir = True
    while seguir:

        # -- Leer funcion ---------------------------------------------------
        print("-" * 62)
        print("  Ingrese los datos del problema:")
        print()
        f, expr = leer_funcion()

        # -- Leer intervalo [a, b] ------------------------------------------
        print()
        a_val, a_str = leer_numero("  a (extremo izquierdo) = ", "a")
        b_val, b_str = leer_numero("  b (extremo derecho)   = ", "b")

        while b_val <= a_val:
            print(
                f"  b debe ser mayor que a.  "
                f"(a = {a_str},  b ingresado = {b_str})"
            )
            b_val, b_str = leer_numero("  b (extremo derecho)   = ", "b")

        # -- Leer n ---------------------------------------------------------
        print()
        n = leer_entero_positivo("  n (numero de subintervalos, entero positivo) = ")

        # -- Mostrar datos ingresados ----------------------------------------
        print()
        print("-" * 62)
        print("  Datos ingresados:")
        print(f"    f(x)      =  {expr}")
        print(f"    Intervalo =  [{a_str}, {b_str}]")
        print(f"    n         =  {n}")
        print(f"    Delta_x   =  ({b_str} - {a_str}) / {n}  =  {(b_val - a_val) / n:.6f}")

        # -- Ejecutar algoritmo ---------------------------------------------
        print()
        try:
            L, tabla, delta_x, S = sumas_inferiores(f, a_val, b_val, n)
        except Exception as e:
            print(f"  Error al evaluar f(x) en el intervalo dado: {e}")
            print("  Verifique que la funcion este bien definida en [a, b].")
            print()
            continue

        # -- Imprimir tabla -------------------------------------------------
        imprimir_tabla(tabla, delta_x, S, L)

        # -- Resultado final ------------------------------------------------
        print()
        print("  Resultado:")
        print(f"    L(A)  aprox  {L:.6f}")
        print()

        # -- Repetir? -------------------------------------------------------
        print("-" * 62)
        resp = input("  Desea calcular otra suma inferior? (s/n): ").strip().lower()
        seguir = resp in ("s", "si")
        print()

    print("  Hasta luego!")
    print("=" * 62)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nPrograma terminado por el usuario.")