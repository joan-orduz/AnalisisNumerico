# Método de Gauss-Seidel con validacion

def es_dominante(A):
    n = len(A)
    for i in range(n):
        suma = sum(abs(A[i][j]) for j in range(n) if j != i)
        if abs(A[i][i]) < suma:
            return False
    return True


def determinante(A):
    # Usamos eliminación para calcular determinante
    n = len(A)
    M = [fila[:] for fila in A]
    det = 1
    
    for i in range(n):
        if M[i][i] == 0:
            return 0
        
        for j in range(i+1, n):
            factor = M[j][i] / M[i][i]
            for k in range(i, n):
                M[j][k] -= factor * M[i][k]
        
        det *= M[i][i]
    
    return det


def gauss_seidel(A, b, x0, tol, max_iter):
    n = len(A)
    x = x0[:]
    
    k = 1
    
    while k <= max_iter:
        x_new = x[:]
        
        for i in range(n):
            suma1 = sum(A[i][j] * x_new[j] for j in range(i))
            suma2 = sum(A[i][j] * x[j] for j in range(i+1, n))
            
            if A[i][i] == 0:
                raise ZeroDivisionError(f"División por cero en A[{i}][{i}]")
            
            x_new[i] = (b[i] - suma1 - suma2) / A[i][i]
        
        error = max(abs(x_new[i] - x[i]) for i in range(n))
        
        print(f"Iteración {k}: {x_new} | Error = {error}")
        
        if error < tol:
            return x_new, True, k
        
        k += 1
        x = x_new[:]
    
    return x, False, max_iter


if __name__ == "__main__":
    try:
        print("Método de Gauss-Seidel")
        
        # n
        while True:
            try:
                n = int(input("Número de ecuaciones/variables: "))
                if n <= 0:
                    print("Error: Debe ser positivo.")
                    continue
                break
            except ValueError:
                print("Error: Ingrese un entero válido.")
        
        # Matriz A
        print("\nIngrese la matriz A:")
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
        
        # PASO 0: validaciones importantes
        print("\nVerificando condiciones...")
        
        if not es_dominante(A):
            print("Advertencia: La matriz NO es diagonalmente dominante.")
            print("El método podría no converger.")
        
        detA = determinante(A)
        if detA == 0:
            print("Error: El determinante es 0. El sistema no tiene solución única.")
            exit()
        
        print(f"✓ Determinante ≠ 0 (det = {detA})")
        
        # Vector b
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
        
        # x0
        print("\nIngrese el vector inicial x0:")
        x0 = []
        for i in range(n):
            while True:
                try:
                    val = float(input(f"x0[{i}] = "))
                    x0.append(val)
                    break
                except ValueError:
                    print("Error: Número inválido.")
        
        # tolerancia
        while True:
            try:
                tol = float(input("\nTolerancia (e): "))
                if tol <= 0:
                    print("Error: Debe ser positiva.")
                    continue
                break
            except ValueError:
                print("Error: Número inválido.")
        
        # iteraciones
        while True:
            try:
                max_iter = int(input("Máximo número de iteraciones: "))
                if max_iter <= 0:
                    print("Error: Debe ser positivo.")
                    continue
                break
            except ValueError:
                print("Error: Ingrese un entero válido.")
        
        # Ejecutar
        solucion, convergio, iteraciones = gauss_seidel(A, b, x0, tol, max_iter)
        
        if convergio:
            print("\n✓ El método convergió")
            print(f"Iteraciones: {iteraciones}")
            for i in range(n):
                print(f"x[{i}] = {solucion[i]:.10f}")
        else:
            print("\n✗ Fracaso: no se alcanzó la tolerancia")
            for i in range(n):
                print(f"x[{i}] = {solucion[i]:.10f}")
    
    except KeyboardInterrupt:
        print("\n\nPrograma interrumpido por el usuario.")
    
    except Exception as e:
        print(f"\nError inesperado: {e}")
