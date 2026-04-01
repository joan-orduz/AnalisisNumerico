#import sympy as sp

def factorizacion_LU(A):
    n = len(A)
    
    # Inicializar matrices
    L = [[0]*n for _ in range(n)]
    U = [fila[:] for fila in A]  # copia de A
    P = [[0]*n for _ in range(n)]
    
    # Inicializar P como identidad
    for i in range(n):
        P[i][i] = 1
    
    for k in range(n):
        # 2.1 búsqueda del pivote
        max_fila = max(range(k, n), key=lambda i: abs(U[i][k]))
        
        # 2.2 chequeo de singularidad
        if U[max_fila][k] == 0:
            return None, None, None, True
        
        # 2.3 intercambio de filas
        if k != max_fila:
            U[k], U[max_fila] = U[max_fila], U[k]
            P[k], P[max_fila] = P[max_fila], P[k]
            L[k], L[max_fila] = L[max_fila], L[k]
        
        # 2.4 eliminación
        for i in range(k+1, n):
            factor = U[i][k] / U[k][k]
            L[i][k] = factor
            for j in range(k, n):
                U[i][j] -= factor * U[k][j]
    
    # Diagonal de L en 1
    for i in range(n):
        L[i][i] = 1
    
    return L, U, P, False


def sustitucion_progresiva(L, b):
    n = len(L)
    y = [0]*n
    
    for i in range(n):
        suma = sum(L[i][j]*y[j] for j in range(i))
        y[i] = b[i] - suma
    
    return y


def sustitucion_regresiva(U, y):
    n = len(U)
    x = [0]*n
    
    for i in range(n-1, -1, -1):
        suma = sum(U[i][j]*x[j] for j in range(i+1, n))
        if U[i][i] == 0:
            raise ZeroDivisionError("División por cero en sustitución regresiva")
        x[i] = (y[i] - suma)/U[i][i]
    
    return x


def multiplicar_matriz_vector(P, b):
    return [sum(P[i][j]*b[j] for j in range(len(b))) for i in range(len(b))]


if __name__ == "__main__":
    try:
        print("Ingrese la matriz A:")
        
        # Validar tamaño
        while True:
            try:
                n = int(input("Número de filas/columnas: "))
                if n <= 0:
                    print("Error: Debe ser positivo.")
                    continue
                break
            except ValueError:
                print("Error: Ingrese un entero válido.")
        
        A = []
        for i in range(n):
            fila = []
            for j in range(n):
                while True:
                    try:
                        val = float(input(f"A[{i}][{j}] = "))
                        fila.append(val)
                        break
                    except ValueError:
                        print("Error: Número inválido.")
            A.append(fila)
        
        print("\nIngrese el vector b:")
        b = []
        for i in range(n):
            while True:
                try:
                    val = float(input(f"b[{i}] = "))
                    b.append(val)
                    break
                except ValueError:
                    print("Error: Número inválido.")
        
        print("\nFactorizando A = P⁻¹LU ...")
        
        L, U, P, singular = factorizacion_LU(A)
        
        # 3. chequeo de singularidad
        if singular:
            print("Error: La matriz es singular. No se puede factorizar.")
            exit()
        
        print("\n✓ Factorización exitosa")
        
        print("\nMatriz L:")
        for fila in L:
            print(fila)
        
        print("\nMatriz U:")
        for fila in U:
            print(fila)
        
        print("\nMatriz P:")
        for fila in P:
            print(fila)
        
        # Resolver sistema
        print("\nResolviendo sistema...")
        
        Pb = multiplicar_matriz_vector(P, b)
        y = sustitucion_progresiva(L, Pb)
        x = sustitucion_regresiva(U, y)
        
        print("\n✓ Solución del sistema Ax = b:")
        for i in range(n):
            print(f"x[{i}] = {x[i]:.10f}")
    
    except KeyboardInterrupt:
        print("\n\nPrograma interrumpido por el usuario.")
    
    except ZeroDivisionError as e:
        print(f"\nError matemático: {e}")
    
    except Exception as e:
        print(f"\nError inesperado: {e}")
