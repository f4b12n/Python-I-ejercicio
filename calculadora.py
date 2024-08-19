def suma(a , b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a , b):
    return a + b

def division(a , b):
    if b != 0:
        return a/b
    else:
        return "Error al dividir por 0"

def mostrar_menu():
    print("Calculadora")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicaciòn")
    print("4. Division")
    print("5. Salir")

while True:
    mostrar_menu()
    opcion = input("Elige una opcion: ")
    if opcion == "5":
        print("Saliendo del proceso")
        break
    
    if opcion in ["1", "2", "3", "4"]:
        num1 = float (input("Ingrese el primer numero: "))
        num2 = float (input("Ingrese el segundo numero: "))
        
        if opcion == "1":
            print(f'Resultado: {suma(num1, num2)}')
        elif opcion == "2":
            print(f'Resultado: {resta(num1, num2)}')
        elif opcion == "3":
            print(f'Resultado: {multiplicacion(num1, num2)}')
        elif opcion == "4":
            print(f'Resultado: {division(num1, num2)}')
    else:
        print("Opcion no valida, por favor intenta de nuevo")
            
