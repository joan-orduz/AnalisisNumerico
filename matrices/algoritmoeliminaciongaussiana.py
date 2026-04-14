from fractions import Fraction

# -----------------------------------
# CONVERTIR NÚMERO
# -----------------------------------
def convertir_numero(valor):
    """
    Convierte un valor a número.
    Acepta:
    - enteros: 2, -5
    - decimales: 2.5, -1.75
    - fracciones: 1/2, -3/4
    """
    try:
        return float(Fraction(valor))
    except:
        raise ValueError(f"Valor inválido: {valor}")


# -----------------------------------
# IMPRIMIR MATRIZ
# -----------------------------------
def imprimir_matriz(A):
    print("\nMatriz actual:")
    for fila in A:
        print(["{:.4f}".format(x) for x in fila])
    print()


# -----------------------------------
# LEER MATRIZ DESDE ARCHIVO
# -----------------------------------
def leer_matriz_desde_archivo(nombre_archivo):
    A = []

    try:
        with open(nombre_archivo, "r") as archivo:
            for linea in archivo:
                if linea.strip() == "":
                    continue

                fila_texto = linea.strip().split()
                fila = [convertir_numero(x) for x in fila_texto]
                A.append(fila)

    except FileNotFoundError:
        print("Error: archivo no encontrado.")
        return None
    except ValueError as e:
        print("Error en el archivo:", e)
        return None

    return A


# -----------------------------------
# LEER MATRIZ MANUALMENTE
# -----------------------------------
def leer_matriz_manual():
    while True:
        try:
            n = int(input("\nIngrese el número de ecuaciones / variables: "))
            if n <= 0:
                print("Error: n debe ser mayor que 0.")
                continue
            break
        except ValueError:
            print("Error: debe ingresar un número entero.")

    A = []

    print("\nIngrese la matriz aumentada fila por fila.")
    print(f"Cada fila debe tener {n+1} valores separados por espacio.")
    print("Puede usar enteros, decimales o fracciones.")
    print("Ejemplo: 2  -3.5  1/2  7\n")

    for i in range(n):
        while True:
            try:
                fila_texto = input(f"Fila {i+1}: ").split()

                if len(fila_texto) != n + 1:
                    print(f"Error: debe ingresar exactamente {n+1} valores.")
                    continue

                fila = [convertir_numero(x) for x in fila_texto]
                A.append(fila)
                break

            except ValueError as e:
                print("Error:", e)
                print("Intente nuevamente.")

    return A


# -----------------------------------
# CARGAR MATRIZ DESDE ARCHIVO
# -----------------------------------
def cargar_desde_archivo(nombre_archivo):
    datos = []
    try:
        with open(nombre_archivo, "r") as archivo:
            for num_linea, linea in enumerate(archivo, start=1):
                linea = linea.strip()
                if not linea:
                    continue
                fila_texto = linea.split()
                try:
                    fila = [convertir_numero(x) for x in fila_texto]
                except ValueError:
                    raise ValueError(f"Línea {num_linea}: valor no numérico")
                if fila:
                    datos.append(fila)
    except FileNotFoundError:
        print("Error: archivo no encontrado.")
        return None, None
    
    if not datos:
        print("Error: el archivo está vacío.")
        return None, None
    
    n = len(datos)
    columnas = len(datos[0])
    
    # Validar que todas las filas tengan el mismo número de columnas
    for i, fila in enumerate(datos):
        if len(fila) != columnas:
            print(f"Error: Fila {i+1} tiene {len(fila)} elementos pero fila 1 tiene {columnas}.")
            return None, None
    
    # Detectar formato
    if columnas == n:
        # Matriz cuadrada N×N
        A = datos
        b = None
        formato = "cuadrada"
    elif columnas == n + 1:
        # Matriz aumentada N×(N+1)
        A = [fila[:-1] for fila in datos]
        b = [fila[-1] for fila in datos]
        formato = "aumentada"
    else:
        print(f"Error: Formato no reconocido ({n} filas y {columnas} columnas).")
        print(f"Esperado: {n}×{n} (cuadrada) o {n}×{n+1} (aumentada).")
        return None, None
    
    return (A, b, formato), True

# -----------------------------------
# VALIDAR MATRIZ AUMENTADA
# -----------------------------------
def validar_matriz(A):
    if A is None or len(A) == 0:
        return False, "Error: la matriz está vacía."

    n = len(A)

    for fila in A:
        if len(fila) != n + 1:
            return False, "Error: la matriz debe ser de tamaño n x (n+1)."

    return True, ""


# -----------------------------------
# ELIMINACIÓN GAUSSIANA
# -----------------------------------
def eliminacion_gaussiana(A):
    n = len(A)

    print("\n=== INICIO DEL PROCESO ===")
    imprimir_matriz(A)

    # Eliminación hacia adelante
    for i in range(n - 1):
        print(f"Paso {i+1}: trabajar con la columna {i+1}")

        # Buscar pivote no nulo
        p = i
        while p < n and A[p][i] == 0:
            p += 1

        if p == n:
            return "Fracaso: el sistema no tiene solución única."

        # Intercambiar filas si es necesario
        if p != i:
            print(f"Se intercambia la fila {i+1} con la fila {p+1}")
            A[i], A[p] = A[p], A[i]
            imprimir_matriz(A)

        # Eliminar debajo del pivote
        for j in range(i + 1, n):
            mji = A[j][i] / A[i][i]
            print(f"m({j+1},{i+1}) = {A[j][i]:.4f} / {A[i][i]:.4f} = {mji:.4f}")

            for k in range(i, n + 1):
                A[j][k] = A[j][k] - mji * A[i][k]

            print(f"Fila {j+1} = Fila {j+1} - ({mji:.4f}) * Fila {i+1}")
            imprimir_matriz(A)

    # Verificar último pivote
    if A[n - 1][n - 1] == 0:
        return "Fracaso: el sistema no tiene solución única."

    print("=== MATRIZ TRIANGULAR SUPERIOR ===")
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

    print("\n=== SOLUCIÓN FINAL ===")
    for i in range(n):
        print(f"x{i+1} = {x[i]:.4f}")

    return x


# -----------------------------------
# PROGRAMA PRINCIPAL
# -----------------------------------
print("ELIMINACIÓN GAUSSIANA CON SUSTITUCIÓN HACIA ATRÁS")
print("El programa acepta enteros, decimales y fracciones.\n")

print("Seleccione la forma de ingreso de datos:")
print("1. Leer matriz desde archivo")
print("2. Ingresar matriz fila por fila")

opcion = input("\nIngrese 1 o 2: ")

if opcion == "1":
    nombre_archivo = input("\nIngrese el nombre del archivo: ")
    resultado = cargar_desde_archivo(nombre_archivo)
    
    if resultado[1]:  # Si hubo éxito
        A, b, formato = resultado[0]
        n = len(A)
        if b is None:
            # Matriz cuadrada, convertirla a aumentada
            
            print(f"\nMatriz {n}×{n} cargada (formato {formato}).")
            print("Ingrese el vector b:")
            b = []
            for i in range(n):
                while True:
                    try:
                        valor = float(input(f"b[{i}] = "))
                        b.append(valor)
                        break
                    except ValueError:
                        print("Error: Ingrese un número válido.")
            # Crear matriz aumentada
            A = [A[i] + [b[i]] for i in range(n)]
        else:
            print(f"\nMatriz aumentada {n}×{n+1} cargada (formato {formato}).")
    else:
        opcion = "2"  # Si falla, cambiar a ingreso manual

if opcion == "2":
    A = leer_matriz_manual()

else:
    print("Opción no válida.")
    exit()

# Validar matriz
valida, mensaje = validar_matriz(A)
if not valida:
    print(mensaje)
    exit()

# Resolver sistema
resultado = eliminacion_gaussiana(A)

if isinstance(resultado, str):
    print("\n" + resultado)