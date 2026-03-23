import sympy as sp
# entradas: matriz R triangular superior y vector C
def sustitucion_regresiva(r, c):
    n = len(r)
    x = [0] * n  # vector solución

    # empezamos desde la última ecuación hacia la primera
    for i in range(n - 1, -1, -1):
        suma = 0
        for j in range(i + 1, n):
            suma += r[i][j] * x[j]  # r[i][j] es el coeficiente de x[j]
        x[i] = (c[i] - suma) / r[i][i]  # r[i][i] es el coeficiente de x[i]

    return x

if __name__ == "__main__":
    try:
        # usuario ingresa la matriz R y el vector C
        print("Ingrese la matriz R (triangular superior):")
        # se ingresan las dimensiones de la matriz
        while True:
            try:
                n = int(input("Número de filas/columnas: "))
                if n <= 0:
                    print("Error: El número de filas/columnas debe ser positivo.")
                    continue
                break
            except ValueError:
                print("Error: Ingrese un número entero válido.")
        
        r = []
        # se muestra visualmente la forma de la matriz para que el usuario ingrese los valores
        for i in range(n):
            fila = []
            for j in range(n):
                if j < i:
                    fila.append(0)  # elementos debajo de la diagonal son 0
                else:
                    while True:
                        try:
                            valor = float(input(f"R[{i}][{j}] = "))
                            fila.append(valor)
                            break
                        except ValueError:
                            print("Error: Ingrese un número válido (entero o decimal).")
            r.append(fila)
        
        # Validar que no hay ceros en la diagonal
        print("\nValidando la matriz...")
        for i in range(n):
            if r[i][i] == 0:
                print(f"Error: Elemento diagonal R[{i}][{i}] es cero. No se puede resolver el sistema.")
                exit()
        print("✓ Matriz válida (triangular superior con diagonal no nula)")
        
        print("\nIngrese el vector C:")
        c = []
        for i in range(n):
            while True:
                try:
                    valor = float(input(f"C[{i}] = "))
                    c.append(valor)
                    break
                except ValueError:
                    print("Error: Ingrese un número válido (entero o decimal).")
        
        # se llama a la función de sustitución regresiva
        solucion = sustitucion_regresiva(r, c)
        print("\n✓ La solución del sistema Rx = C es:")
        for i in range(n):
            print(f"x[{i}] = {solucion[i]:.10f}")
    
    except KeyboardInterrupt:
        print("\n\n⚠️  Programa interrumpido por el usuario.")
    except Exception as e:
        print(f"\nError inesperado: {e}")