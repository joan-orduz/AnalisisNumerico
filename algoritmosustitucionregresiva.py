import sympy as sp
import os

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

def cargar_desde_archivo():
    while True:
        try:
            ruta_archivo = input("\nIngrese la ruta del archivo (ej: matriz.txt): ").strip()
            
            if not os.path.exists(ruta_archivo):
                print(f"Error: El archivo '{ruta_archivo}' no existe.")
                print("Intente nuevamente.")
                continue
            
            with open(ruta_archivo, 'r') as archivo:
                lineas = archivo.readlines()
            
            if not lineas:
                print("Error: El archivo está vacío.")
                continue
            
            matriz = []
            for num_linea, linea in enumerate(lineas, 1):
                linea = linea.strip()
                if not linea:
                    continue
                try:
                    fila = [float(x) for x in linea.split()]
                    if not fila:
                        continue
                    matriz.append(fila)
                except ValueError:
                    print(f"Error: La línea {num_linea} contiene valores no numéricos: '{linea}'")
                    break
            else:
                if not matriz:
                    print("Error: No se encontraron datos numéricos en el archivo.")
                    continue
                
                n = len(matriz)
                # Verificar que todas las filas tengan n+1 elementos (n de R + 1 de C)
                filas_validas = all(len(fila) == n + 1 for fila in matriz)
                
                if not filas_validas:
                    print(f"Error: Debe tener {n} filas y {n+1} columnas.")
                    for i, fila in enumerate(matriz):
                        print(f"Fila {i}: {len(fila)} elementos (esperados {n+1})")
                    continue
                
                matriz_valida = True
                for i in range(n):
                    if matriz[i][i] == 0:
                        print(f"Error: Elemento diagonal [{i}][{i}] es cero.")
                        matriz_valida = False
                        break
                
                if not matriz_valida:
                    continue
                
                # Última columna es el vector C
                r = [fila[:-1] for fila in matriz]
                c = [fila[-1] for fila in matriz]
                
                if len(r[0]) != len(r):
                    print(f"Error: La matriz R no es cuadrada (dimensión {len(r)}x{len(r[0])}).")
                    continue
                
                return r, c
                
        except IOError as e:
            print(f"Error de lectura de archivo: {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")

if __name__ == "__main__":
    try:
        print("=" * 60)
        print("MÉTODO DE SUSTITUCIÓN REGRESIVA")
        print("=" * 60)
        print("\n¿Cómo desea ingresar los datos?")
        print("1. Ingreso manual")
        print("2. Cargar desde archivo")
        
        while True:
            opcion = input("\nSeleccione una opción (1 o 2): ").strip()
            if opcion in ['1', '2']:
                break
            else:
                print("Error: Seleccione 1 o 2")
        
        if opcion == '2':
            r, c = cargar_desde_archivo()
            n = len(r)
        else:
            print("\nIngrese la matriz R (triangular superior):")
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
            for i in range(n):
                fila = []
                for j in range(n):
                    if j < i:
                        fila.append(0)
                    else:
                        while True:
                            try:
                                valor = float(input(f"R[{i}][{j}] = "))
                                fila.append(valor)
                                break
                            except ValueError:
                                print("Error: Ingrese un número válido (entero o decimal).")
                r.append(fila)
            
            print("\nValidando la matriz...")
            for i in range(n):
                if r[i][i] == 0:
                    print(f"Error: Elemento diagonal R[{i}][{i}] es cero. No se puede resolver el sistema.")
                    exit()
            print("Matriz válida")
            
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
        
        solucion = sustitucion_regresiva(r, c)
        print("\n" + "=" * 60)
        print("Solución del sistema Rx = C:")
        print("=" * 60)
        for i in range(n):
            print(f"x[{i}] = {solucion[i]:.10f}")
    
    except KeyboardInterrupt:
        print("\nPrograma interrumpido por el usuario.")
    except Exception as e:
        print(f"Error inesperado: {e}")