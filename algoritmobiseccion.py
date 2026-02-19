import math

def algoritmo_biseccion(f, a, b, precision, m):
    """
    Algoritmo de bisección para encontrar raíces de una función
    
    Entradas:
    - f: Función
    - a y b: Extremos del intervalo
    - precision: Tolerancia
    - m: Máximo de iteraciones
    
    Salidas:
    - Éxito: Solución aproximada
    - Fracaso: "No se logró lo deseado"
    """
    
    # Explicar qué significa cada columna
    print("\nEXPLICACI\u00d3N DE LAS COLUMNAS:")
    print("n      = Número de iteración")
    print("An     = Extremo izquierdo del intervalo")
    print("Bn     = Extremo derecho del intervalo") 
    print("f(An)  = Función evaluada en An")
    print("f(Bn)  = Función evaluada en Bn")
    print("Pn     = Punto medio del intervalo")
    print("f(Pn)  = Función evaluada en el punto medio")
    print()
    
    # Imprimir encabezados de la tabla
    print(f"{'n':<3} {'An':<12} {'Bn':<12} {'f(An)':<12} {'f(Bn)':<12} {'Pn':<12} {'f(Pn)':<12}")
    print("-" * 85)
    
    # Inicialización
    i = 1
    FA = f(a)
    FB = f(b)
    
    # Iteraciones del método de bisección
    while i <= m:
        
        # Calcular punto medio
        p = a + (b - a) / 2
        fp = f(p)
        
        # Imprimir fila de la tabla para esta iteración
        print(f"{i:<3} {a:<12.6f} {b:<12.6f} {FA:<12.6f} {FB:<12.6f} {p:<12.6f} {fp:<12.6f}")
        
        # Verificar criterio de convergencia
        if fp == 0 or (b - a) / 2 < precision:
            print(f"\nÉXITO: Se obtuvo una aproximación de P = {p:.6f}")
            return p
        
        # Actualizar intervalo
        if FA * fp > 0:
            a = p
            FA = fp
        else:
            b = p
            FB = fp
        
        # Incrementar contador
        i = i + 1
    
    # Si se alcanzó el máximo de iteraciones sin convergencia
    print(f"\nFRACASO: No se logró la precisión deseada después de {m} iteraciones")
    return None

def definir_funcion():
    """Permite al usuario definir una función matemática"""
    print("Ingrese la función matemática f(x)")
    print("Puede usar: sin, cos, tan, exp, log, sqrt, x**n, +, -, *, /, (), etc.")
    
    expresion = input("f(x) = ")
    
    def f(x):
        # Hacer disponibles las funciones matemáticas
        return eval(expresion, {"__builtins__": {}, "x": x, "sin": math.sin, 
                               "cos": math.cos, "tan": math.tan, "exp": math.exp, 
                               "log": math.log, "sqrt": math.sqrt, "pi": math.pi, 
                               "e": math.e, "abs": abs})
    
    return f

def main():
    """Función principal para ejecutar el algoritmo de bisección"""
    print("ALGORITMO DE BISECCIÓN")
    print("=" * 30)
    
    # Definir la función
    f = definir_funcion()
    
    # Solicitar extremos del intervalo
    print("\nIngrese los extremos del intervalo:")
    a = float(input("a = "))
    b = float(input("b = "))
    
    # Verificar que f(a) y f(b) tengan signos opuestos
    if f(a) * f(b) >= 0:
        print("Error: f(a) y f(b) deben tener signos opuestos para garantizar una raíz en el intervalo")
        return
    
    # Solicitar precisión y máximo de iteraciones
    precision = float(input("Precisión (tolerancia): "))
    m = int(input("Máximo de iteraciones: "))
    
    # Ejecutar algoritmo
    algoritmo_biseccion(f, a, b, precision, m)

if __name__ == "__main__":
    main()