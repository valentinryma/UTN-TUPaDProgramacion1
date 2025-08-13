# 1.
print("Hola Mundo")

# 2.
nombre = input("Ingrese su nombre: ")

print(f"Hola {nombre}!")

# 3
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
pais = input("Ingrese el nombre del pais de su residencia: ")

print(f"Soy {nombre} {apellido}, tengo {edad} y vivo en {pais}")

# 4
import math

radio = float(input("Ingrese el radio del círculo: "))
perimetro = 2 * math.pi * radio
area = math.pi * (radio ** 2)

print(f"El area es: {area}")
print(f"El perimetro es: {perimetro}")

# 5.
segundos = int(input("Ingrese la cantdida de segundos: "))

horas = segundos / 60 / 60

print(f"{segundos} segundos equivalen a {horas} horas")

# 6
numero = int(input("Ingrese le número al cual mostrar su tabla de multiplicación: "))

print(f"{numero} x 1 = {numero}")
print(f"{numero} x 2 = {numero * 2}")
print(f"{numero} x 3 = {numero * 3}")
print(f"{numero} x 4 = {numero * 4}")
print(f"{numero} x 5 = {numero * 5}")
print(f"{numero} x 6 = {numero * 6}")
print(f"{numero} x 7 = {numero * 7}")
print(f"{numero} x 8 = {numero * 8}")
print(f"{numero} x 9 = {numero * 9}")
print(f"{numero} x 10 = {numero * 10}")

# 7
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número (Distinto de 0): "))

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2

print(f"{numero1} + {numero2} = {suma}")
print(f"{numero1} - {numero2} = {resta}")
print(f"{numero1} x {numero2} = {multiplicacion}")
print(f"{numero1} / {numero2} = {division}")

# 8
altura = float(input("Ingrese su altura: "))
peso = float(input("Ingrese su peso: "))

imc = peso / (altura ** 2)

print(f"Su índice de masa corporal es: {imc}")

# 9
tmpCelsius = round(float(input("Ingrese la temperatura en grados Celsius: ")), 2)

tmpFahrenheit = round((9 / 5) * tmpCelsius + 32, 2)

print(f"{tmpCelsius} °C equivalen a {tmpFahrenheit} °F")

# 10
numero1 = float(input("Ingrese el 1er número: "))
numero2 = float(input("Ingrese el 2do número: "))
numero3 = float(input("Ingrese el 3er número: "))

promedio = round((numero1 + numero2 + numero3) / 3, 2)

print(f"El promedio es {promedio}")

