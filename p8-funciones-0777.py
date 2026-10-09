print("Christian garcia Jimenez NC=0068")

# ==============================================================================
# PRÁCTICA 8: FUNCIONES EN PYTHON
# Grupo: Gpo3H_IA_0777
# Alumno No. de Lista: 24
# Archivo: p8-funciones-0777.py
# ==============================================================================


# ==============================================================================
# 1. CONCEPTO BÁSICO Y SINTAXIS
# ==============================================================================
# Definición de una función simple sin parámetros ni valor de retorno.
def saludar_bienvenida():
    """Imprime un mensaje simple de bienvenida."""
    # La instrucción print muestra el texto directo en la consola.
    print("--- Bienvenido al Script de Funciones en Python ---")

# Llamada a la función para ejecutar su contenido.
saludar_bienvenida()


# ==============================================================================
# 2. FUNCIONES CON PARÁMETROS Y RETORNO
# ==============================================================================
# Las funciones reciben valores (parámetros) e intercambian información procesada.

# Ejemplo 1: Saludo con un parámetro
def saludar_persona(nombre):
    # Utiliza f-strings para formatear e incluir variables dentro de la cadena.
    print(f"Hola, {nombre}, bienvenido a la práctica de Python.")

# Ejemplo 2: Operación matemática simple con retorno
def sumar_numeros(a, b):
    # La palabra clave 'return' devuelve el resultado del cálculo hacia donde fue llamada la función.
    return a + b

# Ejemplo 3: Cálculo con múltiples parámetros
def calcular_area_rectangulo(base, altura):
    # Multiplica base por altura y devuelve el área.
    return base * altura

# Ejecución de los ejemplos:
saludar_persona("Carlos")

# Guardamos el valor devuelto por 'sumar_numeros' en una variable.
resultado_suma = sumar_numeros(15, 25)
print(f"Resultado de la suma (15 + 25): {resultado_suma}")

# Calculamos y mostramos directamente el resultado de la función.
area = calcular_area_rectangulo(10.5, 4.0)
print(f"El área del rectángulo (base: 10.5, altura: 4.0) es: {area}")


# ==============================================================================
# 3. PARÁMETROS CON VALORES POR DEFECTO
# ==============================================================================
# Permite asignar valores predeterminados a los parámetros en caso de no ser proporcionados.

# Ejemplo 1: Parámetro con país por defecto
def registrar_usuario(nombre, pais="México"):
    # Si no se envía el argumento 'pais', tomará "México" por defecto.
    print(f"Usuario {nombre} registrado desde el país: {pais}")

# Ejemplo 2: Aplicación de descuento configurable
def calcular_precio_final(precio, descuento=0.10):
    # Aplica un 10% de descuento (0.10) de forma predeterminada.
    precio_con_descuento = precio * (1 - descuento)
    return precio_con_descuento

# Ejemplo 3: Formateador de texto con repetición por defecto
def repetir_mensaje(mensaje, repeticiones=2):
    # Multiplica la cadena por el número especificado de repeticiones.
    return (mensaje + " ") * repeticiones

# Ejecución de ejemplos con y sin enviar los valores opcionales:
registrar_usuario("Ana")                   # Usa el valor por defecto ("México")
registrar_usuario("John", "Estados Unidos") # Sobrescribe el valor por defecto con "Estados Unidos"

print(f"Precio final ($100 con descuento base 10%): ${calcular_precio_final(100)}")
print(f"Precio final ($100 con descuento especial 25%): ${calcular_precio_final(100, 0.25)}")

print(f"Mensaje repetido por defecto: {repetir_mensaje('Python')}")
print(f"Mensaje repetido 4 veces: {repetir_mensaje('IA', 4)}")


# ==============================================================================
# 4. FUNCIONES LAMBDA (ANÓNIMAS)
# ==============================================================================
# Funciones compactas escritas en una sola línea de código sin usar 'def'.

# Definición de función lambda para elevar un número al cuadrado:
# Sintaxis: lambda argumentos : expresion
cuadrado = lambda x: x ** 2

# Uso directo de la función lambda
numero = 6
print(f"El cuadrado de {numero} usando una función lambda es: {cuadrado(numero)}")


# ==============================================================================
# 5. RECURSIVIDAD
# ==============================================================================
# Función que se llama a sí misma para resolver un problema dividiéndolo en casos más pequeños.

def factorial(n):
    """Calcula el factorial de un número n de forma recursiva."""
    # 1. Caso Base: Detiene las llamadas recursivas cuando 'n' es 0 o 1.
    if n == 0 or n == 1:
        return 1
    # 2. Paso Recursivo: La función se llama a sí misma restando 1 al parámetro.
    else:
        return n * factorial(n - 1)

# Cálculo del factorial de 5 -> (5 * 4 * 3 * 2 * 1 = 120)
num_factorial = 5
print(f"El factorial recursivo de {num_factorial} es: {factorial(num_factorial)}")


# ==============================================================================
# 6. DECORADORES EN PYTHON
# ==============================================================================
# Un decorador toma una función como entrada, le añade funcionalidad extra y la devuelve.

# Definición del decorador:
def decorador_log(funcion_original):
    # La función 'envolvente' ejecuta el código adicional antes y después de la función original.
    def funcion_envolvente(*args, **kwargs):
        print("\n[LOG] --- Iniciando la ejecución de la función ---")
        # Se ejecuta la función principal y se guarda su resultado.
        resultado = funcion_original(*args, **kwargs)
        print("[LOG] --- Finalizó la ejecución correctamente ---")
        return resultado
    return funcion_envolvente

# Aplicación del decorador usando el operador @
@decorador_log
def funcion_procesar_datos():
    # Esta es la función original decorada.
    print("Procesando datos en Machine Learning...")

# Llamada a la función decorada
funcion_procesar_datos()


# ==============================================================================
# 7. EJEMPLOS PRÁCTICOS DE CÓDIGO (REFERENCIA DE GUÍAS DE ESTUDIO)
# ==============================================================================
# Integración de ejercicios representativos tomados de los enlaces de referencia.

print("\n=== EJERCICIOS PRÁCTICOS EN UN SOLO ARCHIVO ===")

# --- Ejemplo Práctico 1: Determinar si un número es par o impar ---
def es_par(numero):
    # El operador % calcula el residuo de la división entre 2.
    if numero % 2 == 0:
        return True
    else:
        return False

print(f"¿El número 8 es par?: {es_par(8)}")
print(f"¿El número 7 es par?: {es_par(7)}")


# --- Ejemplo Práctico 2: Encontrar el número mayor de una lista ---
def obtener_maximo(lista_numeros):
    # La función integrada max() evalúa la lista completa.
    return max(lista_numeros)

mis_notas = [85, 92, 78, 96, 88]
print(f"La calificación más alta es: {obtener_maximo(mis_notas)}")


# --- Ejemplo Práctico 3: Filtrar números mayores a un umbral dado ---
def filtrar_mayores(lista, limite):
    # Comprensión de listas para iterar y filtrar datos eficientemente.
    return [num for num in lista if num > limite]

valores = [10, 55, 23, 89, 4, 70]
print(f"Valores de la lista mayores a 50: {filtrar_mayores(valores, 50)}")


# --- Ejemplo Práctico 4: Calcular el promedio de una lista de datos ---
def calcular_promedio(numeros):
    # sum() obtiene la suma total y len() la cantidad total de elementos.
    if len(numeros) == 0:
        return 0
    return sum(numeros) / len(numeros)

datos_ml = [12.5, 14.2, 10.8, 15.6, 13.0]
print(f"Promedio de las mediciones: {calcular_promedio(datos_ml):.2f}")


# --- Ejemplo Práctico 5: Mapear valores con Lambda y Map ---
# Transforma cada elemento de una lista aplicando una lambda a cada uno.
precios_base = [10, 20, 30, 40]
# La lambda multiplica cada precio por 1.16 para sumar el IVA del 16%.
precios_con_iva = list(map(lambda p: p * 1.16, precios_base))
print(f"Precios originales: {precios_base}")
print(f"Precios con IVA aplicados vía Map/Lambda: {precios_con_iva}")


# --- Ejemplo Práctico 6: Contar vocales en una cadena de texto ---
def contar_vocales(texto):
    vocales = "aeiouAEIOU"
    contador = 0
    # Recorremos letra por letra la cadena recibida.
    for letra in texto:
        if letra in vocales:
            contador += 1
    return contador

frase = "Inteligencia Artificial"
print(f"Número de vocales en '{frase}': {contar_vocales(frase)}")

print("Christian garcia Jimenez NC=0068")