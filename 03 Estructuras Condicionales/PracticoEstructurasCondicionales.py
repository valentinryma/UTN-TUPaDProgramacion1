# 1) ==========================================

edad = float(input("Ingrese la edad del usuario: "))

if edad > 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")

# 2) ==========================================

nota = float(input("Ingrese su nota: "))

if nota >= 6:
    print("Aprobado")
else:
    print("Aprobado")

# 3) ==========================================
numero = float(input("Ingrese un número: "))

if numero % 2:
    print("Ha ingresado un número impar")
else:
    print("Ha ingresado un número par")

# 4) ==========================================

edad = float(input("Ingrese su edad: "))

if edad < 12:
    print("Niño/a")
elif edad < 18:
    print("Adolescente")
elif edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")

# 5) ==========================================

contrasenia = input("Ingrse una contraseña: ")

longitud = len(contrasenia)

if longitud >= 8 or longitud <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# 6) ==========================================

# Importo la libreria necesaria para el punto 6.
from random import randint
from statistics import mode, median, mean

numerosAleatorios = [ randint(1, 100) for i in range(50) ]

# Obtengo la moda, media y mediana.
moda = mode(numerosAleatorios)
media = mean(numerosAleatorios)
mediana = median(numerosAleatorios)

print(f"Moda: {moda} - Media: {media} - Medaiana: {mediana}")

if moda == media == mediana:
    print("(=) Sin sesgo")
elif media > mediana > moda:
    print("(+) Sesgo positivo")
elif media < mediana < moda:
    print("(-) Sesgo negativo")
else:
    # Se puede dar el caso donde: media > moda > mediana
    # el cual no entra en ninguna de las 3 condiciones.
    print("(X) No cumple")

# 7) ==========================================

frase = input("Ingrese una frase o palabra: ")

longFrase = len(frase)

# Valido que no ingrese a una frase vacia ('Indice fuera de rango' lanzá error.)
if (longFrase > 0):
    # Obtengo la ultima letra, contando la longitud de la frase/palabra
    # y restandole uno ya que los arrays, strings empiezan a contar desde 0.
    ultimaLetra = frase[ longFrase - 1].lower()

    if ultimaLetra == "a" or ultimaLetra == "e" or ultimaLetra == "i" or ultimaLetra == "o" or ultimaLetra == "u":
        frase += "!"

print(frase)

# 8) ==========================================

nombre = input("Ingrese su nombre: ")

print("\n1) Nombre en mayúsculas. ")
print("2) Nombre en minúsculas. ")
print("3) Nombre con primera letra en Mayúscula. \n")

opcion = int(input("Ingrese su opción: "))

# Validación
if opcion >= 1 and opcion <= 3:
    if opcion == 1:
        print(nombre.upper())
    elif opcion == 2:
        print(nombre.lower())
    else:
        print(nombre.title())
else:
    print("Opción invalida.")

# 9) ==========================================

magnitud = int(input("Ingrese la magnitud del terremoto: "))

if (magnitud < 3):
    print("Muy Leve")
elif (magnitud < 4):
    print("Leve")
elif (magnitud < 5):
    print("Moderado")
elif (magnitud < 6):
    print("Fuerte")
elif (magnitud < 7):
    print("Muy Fuerte")
else:
    print("Extremo")

# 10 =========================================

emisferio = input("Ingrese el emisferio en el que se enecuentra (N/S): ").lower()
mes = input("Ingrese el mes: ").lower()
dia = int(input("Ingrese el dia: "))

# Válido el dia
if dia > 0 and dia <= 31:
    # Valido el emisferio
    if emisferio == "n":
        # Evaluo el mes y el dia para obtener la estación
        # Algunos dias de diciembre, todo enero o febrero o algnuos dias de marzo.
        if (mes == "diciembre" and dia >= 21) or (mes == "enero" or mes == "febrero") or (mes == "marzo" and dia < 21):
            print("Invierno")
        elif (mes == "marzo" and dia >= 21) or (mes == "abril" or mes == "mayo") or (mes == "junio" and dia < 21):
            print("Primavera")
        elif (mes == "junio" and dia >= 21) or (mes == "julio" or mes == "agosto") or (mes == "septiembre" and dia < 21):
            print("Verano")
        elif (mes == "junio" and dia >= 21) or (mes == "octubre" or mes == "noviembre") or (mes == "diciembre" and dia < 21):
            print("Otoño")
        else:
            print("Mes no válido")
    elif emisferio == "s":
        if (mes == "diciembre" and dia >= 21) or (mes == "enero" or mes == "febrero") or (mes == "marzo" and dia < 21):
            print("Verano")
        elif (mes == "marzo" and dia >= 21) or (mes == "abril" or mes == "mayo") or (mes == "junio" and dia < 21):
            print("Otoño")
        elif (mes == "junio" and dia >= 21) or (mes == "julio" or mes == "agosto") or (mes == "septiembre" and dia < 21):
            print("Invierno")
        elif (mes == "septiembre" and dia >= 21) or (mes == "octubre" or mes == "noviembre") or (mes == "diciembre" and dia < 21):
            print("Primavera")
        else:
            print("Mes no válido")
    else:
        print("Emisferio no válido.")
else:
    print("Dia no válido.")