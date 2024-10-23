import sys

# Obtener números de los argumentos de la línea de comandos
if len(sys.argv) != 3:
    print("Uso: python webserver.py <num1> <num2>")
    sys.exit(1)

num1 = float(sys.argv[1])
num2 = float(sys.argv[2])

# Calcular la suma
suma = num1 + num2

# Mostrar el resultado
print(f"La suma de {num1} y {num2} es: {suma}")
