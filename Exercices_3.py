"""
EJERCICIO #1
Funcion que pida un monto en dinero, decimal o no, y que devuelva el monto mas el 16 de IVA
"""
value = int(input("Ingrese un monto deseado: "))
IVA = (value * .16)

print(str(value + IVA))

"""
EJERCICIO #2
Funcion que pida tres numeros y encuentre el mayor
"""
def numbers(num1, num2, num3):
    if(num1 > num2):
        if(num1 > num3):
            return(num1)
    if(num2 > num1):
        if(num2 > num3):
            return(num2)
    if(num3 > num1):
        if(num3 > num2):
            return(num3)

number1 = int(input("Ingrese un número: "))
number2 = int(input("Ingrese otro número: "))
number3 = int(input("Ingrese otro número: "))

print("El numero mayor encontrado es: ", numbers(number1, number2, number3))
    
"""
EJERCICIO #3
Funcion que pida N numeros y los multiplique todos
"""
def multiply(numbs):
    mult = int(1)
    cont = int
    for i in range(0, numbs):
        numb = int(input("Ingrese un número"))
        mult *= numb
    return(mult)

val = int(input("Ingrese el número de valores a multiplicar"))
print("Su resultado es: " + multiply(val))

"""
EJERCICIO #4
Funcion que calcule el factorial de un numero
"""
def factorial(valor, acumulator):
    conta = valor
    for k in range(0, conta):
        acumulator = (acumulator * valor)
        valor = int(valor -1)
    return(acumulator)

numeros = int(input("¿De cuantos números desea calcular su factorial?: "))
conta = int(0)
acumulator= int(1)

for k in range (0, numeros):
    numero = int(input("Ingrese un número: "))
    print("El factorial de ",numero, "es", factorial(numero, acumulator) )
    
"""
EJERCICIO #5
Pide un string y debera imprimirse en orden reverso
ejemplo: "Uriel se encuentra ocupado"
Salida: "ocupado encuentra se Uriel"
"""

def reverse(text):
    words = text.split('')
    word = ""

    for j in words[::-1]:
        word += j + " "
    print(word)

texto = str(input("Ingrese algún texto: "))
print(reverse(texto))