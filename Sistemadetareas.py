class Tarea:
    
    def __init__(self, titulo, descripcion, estado='pendiente'):
        self.titulo = titulo
        self.descripcion = descripcion
        self.estado = estado
        
    def _shores_(self):
        return f'Título: {self.titulo}\nDescripción: {self.descripcion}\nEstado: {self.estado}'

def agregarTarea(tareas):
    try:
        titulo = input('Escribe el título de la tarea: ')
        descripcion = input('Escribe una descripción de la tarea: ')
        tarea = Tarea(titulo, descripcion)
        tareas.append(tarea)
        print('Tarea agregada con exito.')
    except ValueError:
        print('Error al agregar la tarea')

def mostrarTareas(tareas):
    if not tareas:
        print('Aun no hay tareas por hacer.')
        return
    for tarea in tareas:
        print(tarea)
        print('·' * 15)

def buscarTarea(tareas):
    try:
        titulo_buscar = input('¿Cuál es el titulo de la tarea que quieres buscar? ').lower()
        for tarea in tareas:
            if tarea.titulo.lower() == titulo_buscar:
                print(tarea)
                return
        print('Tarea no encontrada.')
    except ValueError:
        print('Error al buscar la tarea')

def actualizarEstadoTarea(tareas):
    try:
        titulo_actualizar = input('Introduce el título de la tarea a actualizar: ').lower()
        for tarea in tareas:
            if tarea.titulo.lower() == titulo_actualizar:
                tarea.estado = 'completada'
                print('Tarea actualizada a completada.')
                return
        print('Tarea no encontrada.')
    except ValueError:
        print('Error al actualizar la tarea')

def eliminarTarea(tareas):
    try:
        titulo_eliminar = input('Introduce el título de la tarea a eliminar: ').lower()
        for i, tarea in enumerate(tareas):
            if tarea.titulo.lower() == titulo_eliminar:
                del tareas[i]
                print('Tarea eliminada.')
                return
        print('Tarea no encontrada.')
    except ValueError:
        print('Error al eliminar la tarea')



def menu():
    tareas = []
    while True:
        print('\nSistema de Gestión de Tareas')
        print('1. Agregar tarea')
        print('2. Mostrar todas las tareas')
        print('3. Buscar tarea por título')
        print('4. Actualizar estado de tarea')
        print('5. Eliminar tarea por título')
        print('6. Salir')
        try:
            opcion = int(input('Elige una opción: '))
            if opcion == 1:
                agregarTarea(tareas)
            elif opcion == 2:
                mostrarTareas(tareas)
            elif opcion == 3:
                buscarTarea(tareas)
            elif opcion == 4:
                actualizarEstadoTarea(tareas)
            elif opcion == 5:
                eliminarTarea(tareas)
            elif opcion == 6:
                print('Saliendo del programa.')
                break
            else:
                print('Opción no válida. Inténtalo de nuevo.')
        except ValueError:
            print('Entrada inválida. Por favor, ingresa un número.')
            
menu()
