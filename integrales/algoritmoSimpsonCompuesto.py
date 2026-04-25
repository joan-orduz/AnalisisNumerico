import math

def simpson_compuesto (f, a, b, n):
    print("\nCalculando la integral usando el método de Simpson compuesto...")
    print(f"Intervalo: [{a}, {b}]")
    print(f"Número de subintervalos (n): {n}")
    h = (b - a) / n
    S0 = f(a) + f(b)
    S1 = 0
    S2 = 0
    for i in range(1, n):
        x_i = a + i * h
        if i % 2 == 0:
            S2 += f(x_i)
        else:
            S1 += f(x_i)
    return (h / 3) * (S0 + 4 * S1 + 2 * S2)

if __name__ == "__main__":
    # Entradas:
    # f (funcion)
    # a y b (intervalo de integracion)
    # m numero de intervalos (Tomamos n = 2m para que el intervalo pueda ser cualquiera)
    print("=" * 60)
    print("ALGORITMO DE SIMPSON COMPUESTO")
    print("=" * 60)
    print("\nIngrese la función a integrar (en términos de x):")
    # El usuario ingresa la funcion en terminos de x pero hay que comprobar errores
    while True:
        try:
            func_input = input("f(x) = ").strip()
            f = lambda x: eval(func_input)
            # Prueba de la función con un valor de x
            f(0)
            break
        except Exception as e:
            print(f"Error en la función: {e}. Intente nuevamente.")

    print("\nIngrese el intervalo de integración:")
    # verificar que sean intervalos validos
    while True:
        try:
            a = float(input("a = "))
            b = float(input("b = "))
            if a >= b:
                print("Error: El límite inferior debe ser menor que el límite superior.")
            else:
                break
        except ValueError:
            print("Error: Ingrese valores numéricos válidos.")

    print("\nIngrese el número de subintervalos:")
    # acá hacemos trampa y tomamos n = 2m, para que el intervalo pueda ser cualquiera pero primero verificamos que la entrada sea valida
    while True:
        try:
            m = int(input("m = "))
            if m <= 0:
                print("Error: El número de subintervalos debe ser un entero positivo.")
            else:
                break
        except ValueError:
            print("Error: Ingrese un número entero válido.")
    n = 2 * m  # Aseguramos que n sea par
    # Cálculo de la integral usando el método de Simpson compuesto
    resultado = simpson_compuesto(f, a, b, n)
    print(f"\nEl resultado de la integral es: {resultado}")