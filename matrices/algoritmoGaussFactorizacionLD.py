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
# Carga matriz desde archivo.
# Detecta automáticamente dos formatos:
#   1. Matriz cuadrada N×N (solo A)
#   2. Matriz aumentada N×(N+1) (A | b)
# ─────────────────────────────────────────────
def cargar_desde_archivo(ruta):
    datos = []
    with open(ruta, "r") as f:
        for numero_linea, linea in enumerate(f, start=1):
            linea = linea.strip()
            if not linea:
                continue
            try:
                valores = [float(v) for v in linea.split()]
            except ValueError:
                raise ValueError(
                    f"Línea {numero_linea}: valor no numérico en '{linea}'"
                )
            if not valores:
                continue
            datos.append(valores)

    if not datos:
        raise ValueError("El archivo está vacío.")

    n = len(datos)
    columnas = len(datos[0])

    # Validar consistencia de columnas
    for i, fila in enumerate(datos):
        if len(fila) != columnas:
            raise ValueError(
                f"Fila {i+1} tiene {len(fila)} elementos pero fila 1 tiene {columnas}."
            )

    # Detectar formato
    if columnas == n:
        # Matriz cuadrada N×N (usar como A, pedir b después)
        A = datos
        b = None
        formato = "cuadrada"
    elif columnas == n + 1:
        # Matriz aumentada N×(N+1), separar en A y b
        A = [fila[:-1] for fila in datos]
        b = [fila[-1] for fila in datos]
        formato = "aumentada"
    else:
        raise ValueError(
            f"Formato no reconocido: {n} filas y {columnas} columnas.\n"
            f"Esperado: matriz {n}×{n} (cuadrada) o {n}×{n+1} (aumentada)."
        )

    return A, b, n, formato

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
                    A, b, n, formato = cargar_desde_archivo(ruta)
                    print(f"\nArchivo cargado: matriz {n}×{n} (formato {formato})")
                    print("\nMatriz A:")
                    for fila in A:
                        print(fila)
                    
                    # Si es matriz cuadrada pura, pedir vector b
                    if b is None:
                        print("\nIngrese el vector b:")
                        b = []
                        for i in range(n):
                            while True:
                                try:
                                    valor = float(input(f"b[{i}] = "))
                                    b.append(valor)
                                    break
                                except ValueError:
                                    print("Error: Ingrese un número válido.")
                    
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
