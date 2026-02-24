import math


def algoritmo_newton(f, df, p0, tolerancia, N0):
    """
    Algoritmo del Método de Newton-Raphson para encontrar raíces de una función.

    Entradas:
    - f        : Función f(x) de la cual se busca la raíz f(p) = 0
    - df       : Derivada f'(x) de la función
    - p0       : Aproximación inicial
    - presición: Tolerancia (precisión deseada)
    - M        : Número máximo de iteraciones

    Salidas:
    - Éxito: Se obtuvo una aproximación deseada al punto fijo
    - Fracaso: Despues de M iteraciones NO se logro la presición deseada :(
    """

    print("\nEXPLICACIÓN DE LAS COLUMNAS:")
    print("n      = Número de iteración")
    print("p0     = Aproximación anterior")
    print("f(p0)  = Función evaluada en p0")
    print("f'(p0) = Derivada evaluada en p0")
    print("p      = Nueva aproximación  p = p0 - f(p0)/f'(p0)")
    print("|p-p0| = Error absoluto entre iteraciones consecutivas")
    print()

    print(f"{'n':<5} {'p0':<18} {'f(p0)':<18} {'f´(p0)':<18} {'p':<18} {'|p - p0|':<18}")
    print("-" * 97)

    i = 1
    while i <= N0:

        fp0  = f(p0)
        dfp0 = df(p0)

        # Verificar que la derivada no sea cero (el método fallaría)
        if dfp0 == 0:
            print(f"\nFRACASO: La derivada f'(p0) = 0 en p0 = {p0:.10f}.")
            print("         El método de Newton no puede continuar (división por cero).")
            return None

        # Fórmula de Newton: p = p0 - f(p0) / f'(p0)
        p     = p0 - fp0 / dfp0
        error = abs(p - p0)

        print(f"{i:<5} {p0:<18.10f} {fp0:<18.10f} {dfp0:<18.10f} {p:<18.10f} {error:<18.2e}")

        # Criterio de convergencia
        if error < tolerancia:
            print(f"\nÉXITO: Raíz aproximada encontrada en p = {p:.10f}")
            print(f"       Después de {i} iteraciones con error |p - p0| = {error:.2e}")
            return p

        p0 = p
        i += 1

    print(f"\nFRACASO: No se logró la precisión deseada después de {N0} iteraciones.")
    print(f"         Última aproximación: p = {p0:.10f}")
    return None


def definir_funcion(nombre, descripcion):
    """Permite al usuario definir una función matemática"""
    print(f"\nIngrese la función {descripcion}")
    print("Puede usar: sin, cos, tan, exp, log, sqrt, x**n, +, -, *, /, (), etc.")

    expresion = input(f"{nombre}(x) = ")

    def func(x):
        return eval(expresion, {
            "__builtins__": {},
            "x": x,
            "sin": math.sin,
            "cos": math.cos,
            "tan": math.tan,
            "exp": math.exp,
            "log": math.log,
            "sqrt": math.sqrt,
            "pi": math.pi,
            "e":  math.e,
            "abs": abs
        })

    return func


def main():
    """Función principal para ejecutar el algoritmo de Newton-Raphson"""
    print("ALGORITMO DE NEWTON-RAPHSON")
    print("=" * 40)
    print()
    print("Objetivo: Encontrar p tal que f(p) = 0")
    print("Fórmula:  p_n = p_{n-1} - f(p_{n-1}) / f'(p_{n-1})")
    print()
    print("IMPORTANTE: Necesita ingresar tanto f(x) como su derivada f'(x).")

    # Definir f(x) y f'(x)
    f  = definir_funcion("f",  "f(x)  — función original")
    df = definir_funcion("f'", "f'(x) — derivada de f(x)")

    # Solicitar parámetros
    print("\nIngrese los parámetros del método:")
    p0         = float(input("Aproximación inicial p0 = "))
    tolerancia = float(input("Tolerancia (ej: 0.0001): "))
    N0         = int(input("Máximo de iteraciones: "))

    # Ejecutar algoritmo
    print(f"\n{'='*97}")
    print(f"Iterando con p0 = {p0}, tolerancia = {tolerancia}, max iter = {N0}")
    print(f"{'='*97}")

    algoritmo_newton(f, df, p0, tolerancia, N0)


if __name__ == "__main__":
    main()