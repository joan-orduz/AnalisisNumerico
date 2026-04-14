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
        raise ValueError("El archivo está vacío o no contiene datos válidos.")

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
        import os
        print("Método de Gauss-Seidel")

        # ── Elegir modo de ingreso ──────────────────────────────────────────
        print("\n¿Cómo desea ingresar la matriz?")
        print("  1. Desde un archivo de texto")
        print("  2. Manualmente por teclado")

        while True:
            opcion = input("Opción (1/2): ").strip()
            if opcion in ("1", "2"):
                break
            print("Error: ingrese 1 o 2.")

        # ── Modo 1: desde archivo ───────────────────────────────────────────
        if opcion == "1":
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
                    print("Verifique que el archivo esté en la misma carpeta e intente de nuevo.\n")
                except ValueError as e:
                    print(f"\nError en el archivo: {e}")
                    print("Corrija el archivo o ingrese otro nombre e intente de nuevo.\n")

        # ── Modo 2: ingreso manual (código original intacto) ────────────────
        else:
            # n
            while True:
                try:
                    n = int(input("\nNúmero de ecuaciones/variables: "))
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

        # ── PASO 0: validaciones importantes (lógica original intacta) ──────
        print("\nVerificando condiciones...")

        if not es_dominante(A):
            print("Advertencia: La matriz NO es diagonalmente dominante.")
            print("El método podría no converger.")

        detA = determinante(A)
        if detA == 0:
            print("Error: El determinante es 0. El sistema no tiene solución única.")
            exit()

        print(f"✓ Determinante ≠ 0 (det = {detA})")

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
