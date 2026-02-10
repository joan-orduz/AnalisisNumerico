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
    
    # Paso 0: Sea i = 1, FA = f(a)
    i = 1
    FA = f(a)
    
    # Paso 1: Mientras i <= m, haga de 2 a 5
    while i <= m:
        
        # Paso 2: Sea p = a + (b-a)/2, fp = f(p)
        p = a + (b - a) / 2
        fp = f(p)
        
        # Paso 3: Si fp = 0 ó (b-a)/2 < precisión entonces salida (Éxito)
        if fp == 0 or (b - a) / 2 < precision:
            return p
        
        # Paso 4: Sea i = i + 1
        i = i + 1
        
        # Paso 5: Si (FA)(FP) > 0 -> Entonces: a = p, en caso contrario b = p
        if FA * fp > 0:
            a = p
            FA = fp
        else:
            b = p
    
    # Paso 6: Salida (FRACASO)
    return "No se logró lo deseado"

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
    resultado = algoritmo_biseccion(f, a, b, precision, m)
    
    # Mostrar resultado
    print("\nRESULTADO:")
    if isinstance(resultado, str):
        print(resultado)
    else:
        print(f"Solución aproximada: {resultado}")
        print(f"f({resultado}) = {f(resultado)}")

if __name__ == "__main__":
    main()