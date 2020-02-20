number = int(input("Ingresa un número: "))
number_t = int(input("ingresa otro número: "))

try:
    print(number/number_t)
except ArithmeticError as err:
    print("La operación no pudo ser realizada")
    print("Error: " + str(err))