class Contacto: #definimos la clase y nombre de la clase
    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono
        
def mostrar_menu():
    print('Gestion de contactos')
    print('1. Agregar contacto ')
    print('2. Mostrar contacto ')
    print('3. Buscar contacto ')
    print('4. Eliminar contacto ')
    print('5. Salir')
    
contactos = []

while True:
    mostrar_menu()
    opcion = input("Digite una opcion del 1 al 5: ")
    
    if opcion == "5":
        print("Saliendo del programa. ")
        break
    if opcion == "1":
        nombre = input("Ingrese el contacto: ")
        telefono = input("Ingrese el numero de telefono: ")
        contacto = Contacto(nombre, telefono)
        contactos.append(contacto) #append se utiliza para agregar un elemento a la lista en este caso (contactos)
        print("Contacto agregado.")
    elif opcion == "2":
        for c in contactos:
            print(f'Nombre: {c.nombre}, Telefono: {c.telefono}' )
    elif opcion == "3":
        nombre = input("Ingresa el nombre a buscar: ")
        encontrado = False
        for c in contactos:
            if c.nombre == nombre:
                print(f'Nombre: {c.nombre}, Telefono: {c.telefono}')
                encontrado = True
                break
            if not encontrado:
                print("Contacto no encontrado. ")
    elif opcion == "4":
        nombre = input("Ingresa el nombre a eliminar: ")
        for c in contactos:
            if c.nombre == nombre:
                contactos.remove(c)
                print("Contacto eliminado.")
                break
    else:
        print("opcion no valida. Intenta nuevamente")
    