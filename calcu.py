x = int(input("Escribe un numero: "))
y = int(input("Escribe otro numero: "))

z = int(input("Escribe la opción que deseas: \n"
                "1.- SUMAR \n" 
                "2.- RESTAR \n"
                "3.- MULTIPLICAR \n"))

def sumar(x, y):
    suma = x + y
    print(f"La suma de los valores es: {suma}")



def restar(x, y):
    resta = x - y
    print(f"La resta de los valores es: {resta}")



def multiplicar(x, y):
    mult = x * y
    print(f"La multiplicación de los valores es: {mult}")


if z == 1:
    sumar(x, y)

elif z == 2:
    restar(x, y)

elif z == 3:
    multiplicar(x, y)

else:
    print("Error")
