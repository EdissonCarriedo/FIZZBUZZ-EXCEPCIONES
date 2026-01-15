try:
    numero = int(input("Ingresa un número: "))

    if numero % 3 == 0 and numero % 5 == 0:
     print("FizzBuzz")
    elif numero % 3 == 0:
     print("Fizz")
    elif numero % 5 == 0:
     print("Buzz")
    else:
     print(f"{numero} no es multiplo de 3 y 5")
except ValueError:
 print("Error solo numeros")

