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

# ─────────────────────────────────────────────
# NUEVA FUNCIÓN: carga matriz y vector desde archivo
# Formato esperado del archivo:
#   - Cada fila de la matriz A ocupa una línea con n números separados por espacios.
#   - La última columna de cada fila se interpreta como el término independiente b.
#   Ejemplo (sistema 3x3):
#       2  1 -1  8
#      -3 -1  2 -11
#      -2  1  2  -3
# ─────────────────────────────────────────────
def cargar_desde_archivo(ruta):
    A = []
    b = []
    with open(ruta, "r") as f:
        for numero_linea, linea in enumerate(f, start=1):
            linea = linea.strip()
            if not linea:          # ignorar líneas vacías
                continue
            try:
                valores = [float(v) for v in linea.split()]
            except ValueError:
                raise ValueError(
                    f"Línea {numero_linea}: se encontró un valor no numérico → '{linea}'"
                )
            if len(valores) < 2:
                raise ValueError(
                    f"Línea {numero_linea}: se necesitan al menos 2 valores (coeficientes + término independiente)."
                )
            A.append(valores[:-1])   # todo menos el último → fila de A
            b.append(valores[-1])    # último valor         → componente de b

    if not A:
        raise ValueError("El archivo está vacío o no contiene datos válidos.")

    n = len(A)
    for i, fila in enumerate(A):
        if len(fila) != n:
            raise ValueError(
                f"La matriz no es cuadrada: fila {i+1} tiene {len(fila)} columnas "
                f"pero se esperaban {n} (hay {n} filas)."
            )
    return A, b, n

if __name__ == "__main__":
    try:
        # ── Elegir modo de ingreso ──────────────────────────────────────────
        print("¿Cómo desea ingresar la matriz?")
        print("  1. Desde un archivo de texto")
        print("  2. Manualmente por teclado")
        
        while True:
            opcion = input("Opción (1/2): ").strip()
            if opcion in ("1", "2"):
                break
            print("Error: ingrese 1 o 2.")

        # ── Modo 1: desde archivo ───────────────────────────────────────────
        if opcion == "1":
            import os
            directorio = os.getcwd()
            print(f"(Los archivos se buscan en: {directorio})")
            while True:
                nombre = input("Nombre del archivo (ej: Matriz.txt): ").strip()
                ruta = os.path.join(directorio, nombre)
                try:
                    A, b, n = cargar_desde_archivo(ruta)
                    print(f"\n✓ Archivo cargado correctamente ({n}x{n} con vector b incluido).")
                    print("\nMatriz A:")
                    for fila in A:
                        print(fila)
                    print("\nVector b:", b)
                    break
                except FileNotFoundError:
                    print(f"\nError: No se encontró '{nombre}' en {directorio}")
                    print("Verifique que el archivo esté en la misma carpeta que el .py e intente de nuevo.\n")
                except ValueError as e:
                    print(f"\nError en el archivo: {e}")
                    print("Corrija el archivo o ingrese otra ruta e intente de nuevo.\n")

        # ── Modo 2: ingreso manual (código original intacto) ────────────────
        else:
            print("\nIngrese la matriz A:")
            
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

        # ── Factorización y resolución (lógica original, sin cambios) ───────
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
