def algoritmo_secante(f, x0, x1, precision, max_iter):
    """
    Algoritmo de la secante para encontrar raíces de funciones
    
    Entradas:
    - f: función
    - x0, x1: valores iniciales
    - precision: tolerancia
    - max_iter: máximo de iteraciones
    """
    
    # Inicialización de variables
    x_anterior = x0
    x_actual = x1
    
    # Explicar qué significa cada columna
    print("\nEXPLICACIÓN DE LAS COLUMNAS:")
    print("n        = Número de iteración")
    print("Xn-1     = Valor anterior (punto izquierdo)")
    print("Xn       = Valor actual (punto derecho)")
    print("f(Xn-1)  = Función evaluada en Xn-1")
    print("f(Xn)    = Función evaluada en Xn")
    print("Xn+1     = Nuevo valor calculado (aproximación a la raíz)")
    print("f(Xn+1)  = Función evaluada en la nueva aproximación")
    print("|Xn+1-Xn| = Error absoluto entre iteraciones")
    print()
    
    # Imprimir encabezados de la tabla
    print(f"{'n':<4} {'Xn-1':<12} {'Xn':<12} {'f(Xn-1)':<12} {'f(Xn)':<12} {'Xn+1':<12} {'f(Xn+1)':<12} {'|Xn+1-Xn|':<12}")
    print("-" * 100)
    
    # Iteraciones del método de la secante
    for n in range(1, max_iter + 1):
        
        # Evaluar la función en los puntos actuales
        f_anterior = f(x_anterior)
        f_actual = f(x_actual)
        
        # Verificar que el denominador no sea cero
        denominador = f_actual - f_anterior
        if abs(denominador) < 1e-15:
            print("Error: denominador muy pequeño, división por cero")
            return None
        
        # Calcular el siguiente punto usando la fórmula de la secante
        x_siguiente = (x_anterior * f_actual - x_actual * f_anterior) / denominador
        
        # Evaluar la función en el nuevo punto
        f_siguiente = f(x_siguiente)
        
        # Calcular el error absoluto
        error = abs(x_siguiente - x_actual)
        
        # Imprimir fila de la tabla para esta iteración
        print(f"{n:<4} {x_anterior:<12.6f} {x_actual:<12.6f} {f_anterior:<12.6f} {f_actual:<12.6f} {x_siguiente:<12.6f} {f_siguiente:<12.6f} {error:<12.6f}")
        
        # Verificar criterio de convergencia
        if error < precision:
            print(f"\nÉXITO: Se obtuvo una aproximación de P = {x_siguiente:.6f}")
            return x_siguiente
        
        # Actualizar valores para la siguiente iteración
        x_anterior = x_actual
        x_actual = x_siguiente
    
    # Si se alcanzó el máximo de iteraciones sin convergencia
    print(f"\nFRACASO: No se logró la precisión deseada después de {max_iter} iteraciones")
    return None


# Ejecución interactiva
if __name__ == "__main__":
    import math
    
    print("=== ALGORITMO DE LA SECANTE ===")
    print()
    
    # Solicitar la función al usuario
    print("Ingrese la función f(x) usando la variable 'x'")
    print("Ejemplos:")
    print("  x**2 - 2")
    print("  x**3 - x - 1") 
    print("  math.cos(x) - x")
    print("  math.exp(x) - 2")
    print("  x**2 - 4*x + 3")
    
    expresion = input("\nf(x) = ")
    
    # Crear la función dinámicamente
    def f(x):
        try:
            return eval(expresion)
        except Exception as e:
            print(f"Error evaluando la función: {e}")
            return None
    
    # Solicitar parámetros al usuario
    x0 = float(input("\nIngrese el primer valor inicial (x0): "))
    x1 = float(input("Ingrese el segundo valor inicial (x1): "))
    precision = float(input("Ingrese la precisión deseada (ej: 0.00001): "))
    max_iter = int(input("Ingrese el máximo número de iteraciones: "))
    
    print("\n" + "="*90)
    print("RESULTADOS")
    print("="*90)
    
    # Ejecutar el algoritmo
    resultado = algoritmo_secante(f, x0, x1, precision, max_iter)
