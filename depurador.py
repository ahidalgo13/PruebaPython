# Programa para practicar el depurador de Python (Datos por pantalla)

def calcular_promedio(n1, n2, n3):
    suma = n1 + n2 + n3
    promedio = suma / 3
    return promedio

# Programa principal
print("--- INGRESO DE DATOS ---")
nombre = input("Ingrese el nombre del alumno: ")

# Usamos float() para permitir decimales. Si quisieras solo enteros, usarías int()
nota1 = float(input("Ingrese la Nota 1: "))
nota2 = float(input("Ingrese la Nota 2: "))
nota3 = float(input("Ingrese la Nota 3: "))

# Llamamos a la función
promedio = calcular_promedio(nota1, nota2, nota3)

print("\n--- RESULTADOS ---")
print("Alumno:", nombre)
print("Nota 1:", nota1)
print("Nota 2:", nota2)
print("Nota 3:", nota3)
print("Promedio:", promedio)

if promedio >= 14:
    print("Resultado: APROBADO")
else:
    print("Resultado: DESAPROBADO")