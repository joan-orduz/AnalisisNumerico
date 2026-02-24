import math


def algoritmo_punto_fijo(g, p0, tolerancia, N0):
    """
    Algoritmo de Iteración de Punto Fijo para encontrar raíces de una función.

    Entradas:
    - g        : Función de iteración g(x), tal que el punto fijo p = g(p) es la raíz buscada
    - p0       : Aproximación inicial
    - presicion: Tolerancia (precisión deseada)
    - M       : Número máximo de iteraciones

    Salidas:
    - Éxito: Se obtuvo una aproximación deseada al punto fijo
    - Fracaso: Despues de M iteraciones NO se logro la presición deseada :(
    """

    print("\nEXPLICACIÓN DE LAS COLUMNAS:")
    print("n      = Número de iteración")
    print("p0     = Aproximación anterior (entrada de g)")
    print("p      = Nueva aproximación p = g(p0)")
    print("g(p0)  = Valor de la función g evaluada en p0")
    print("|p-p0| = Error absoluto entre iteraciones consecutivas")
    print()

    print(f"{'n':<5} {'p0':<18} {'p = g(p0)':<18} {'|p - p0|':<18}")
    print("-" * 62)

    i = 1
    while i <= N0:
        p = g(p0)
        error = abs(p - p0)

        print(f"{i:<5} {p0:<18.10f} {p:<18.10f} {error:<18.2e}")

        # Criterio de convergencia
        if error < tolerancia:
            print(f"\nÉXITO: Punto fijo aproximado encontrado en p = {p:.10f}")
            print(f"       Después de {i} iteraciones con error |p - p0| = {error:.2e}")
            return p

        p0 = p
        i += 1

    print(f"\nFRACASO: No se logró la precisión deseada después de {N0} iteraciones.")
    print(f"         Última aproximación: p = {p0:.10f}")
    return None


def definir_funcion(nombre):
    """Permite al usuario definir una función matemática g(x)"""
    print(f"\nIngrese la función {nombre}(x)")
    print("Puede usar: sin, cos, tan, exp, log, sqrt, x**n, +, -, *, /, (), etc.")

    expresion = input(f"{nombre}(x) = ")

    def g(x):
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
            "e": math.e,
            "abs": abs
        })

    return g


def main():
    """Función principal para ejecutar el algoritmo de punto fijo"""
    print("ALGORITMO DE ITERACIÓN DE PUNTO FIJO")
    print("=" * 40)
    print()
    print("NOTA: se debe ingresar la función como x = g(x)")

    # Definir la función g(x)
    g = definir_funcion("g")

    # Solicitar parámetros
    print("\nIngrese los parámetros del método:")
    p0 = float(input("Aproximación inicial p0 = "))
    tolerancia = float(input("Tolerancia (ej: 0.0001): "))
    N0 = int(input("Máximo de iteraciones: "))

    # Ejecutar algoritmo
    print(f"\n{'='*62}")
    print(f"Iterando con p0 = {p0}, tolerancia = {tolerancia}, maximo iteraciones = {N0}")
    print(f"{'='*62}")

    algoritmo_punto_fijo(g, p0, tolerancia, N0)


if __name__ == "__main__":
    main()
