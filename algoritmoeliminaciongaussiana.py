def imprimir_matriz(A):
    print("Matriz actual:")
    for fila in A:
        print(["{:.4f}".format(x) for x in fila])
    print()


def eliminacion_gaussiana(A):
    n = len(A)

    # Verificar que la matriz sea n x (n+1)
    for fila in A:
        if len(fila) != n + 1:
            return "Error: la matriz debe ser de tamaño n x (n+1)."

    print("=== INICIO DEL PROCESO ===")
    imprimir_matriz(A)

    # Eliminación gaussiana
    for i in range(n - 1):
        print(f"Paso {i+1}: trabajar con la columna {i+1}")

        # Buscar pivote
        p = i
        while p < n and A[p][i] == 0:
            p += 1

        # Si no hay pivote, no hay solución única
        if p == n:
            return "Fracaso: el sistema no tiene solución única."

        # Intercambiar filas si es necesario
        if p != i:
            print(f"Intercambio de fila {i+1} con fila {p+1}")
            A[i], A[p] = A[p], A[i]
            imprimir_matriz(A)

        # Eliminar debajo del pivote
        for j in range(i + 1, n):
            mji = A[j][i] / A[i][i]
            print(f"Multiplicador m({j+1},{i+1}) = {A[j][i]:.4f} / {A[i][i]:.4f} = {mji:.4f}")

            for k in range(i, n + 1):
                A[j][k] = A[j][k] - mji * A[i][k]

            print(f"Fila {j+1} = Fila {j+1} - ({mji:.4f}) * Fila {i+1}")
            imprimir_matriz(A)

    # Verificar último pivote
    if A[n - 1][n - 1] == 0:
        return "Fracaso: el sistema no tiene solución única."

    print("=== MATRIZ TRIANGULAR SUPERIOR OBTENIDA ===")
    imprimir_matriz(A)

    # Sustitución hacia atrás
    x = [0] * n

    x[n - 1] = A[n - 1][n] / A[n - 1][n - 1]
    print(f"x{n} = {A[n - 1][n]:.4f} / {A[n - 1][n - 1]:.4f} = {x[n - 1]:.4f}")

    for i in range(n - 2, -1, -1):
        suma = 0
        for j in range(i + 1, n):
            suma += A[i][j] * x[j]

        x[i] = (A[i][n] - suma) / A[i][i]
        print(f"x{i+1} = ({A[i][n]:.4f} - {suma:.4f}) / {A[i][i]:.4f} = {x[i]:.4f}")

    print("=== SOLUCIÓN FINAL ===")
    for i in range(n):
        print(f"x{i+1} = {x[i]:.4f}")

    return x


# ------------------------------
# PROGRAMA PRINCIPAL
# ------------------------------

n = int(input("Ingrese el número de ecuaciones / variables: "))

A = []
print("Ingrese los coeficientes de la matriz aumentada fila por fila:")
print("Debe ingresar", n + 1, "valores por cada fila")

for i in range(n):
    fila = []
    print(f"\nFila {i+1}:")
    for j in range(n + 1):
        valor = float(input(f"Ingrese A[{i+1}][{j+1}]: "))
        fila.append(valor)
    A.append(fila)

resultado = eliminacion_gaussiana(A)

if type(resultado) == str:
    print(resultado)