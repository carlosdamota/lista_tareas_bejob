from colorama import init, Back, Fore, Style

# Inicializa colorama
init(autoreset=True)

class ToDoList:
    contador_id = 0 # Inicializa el contador en 0
    def __init__(self, titulo, descripcion="", estado="Pendiente"): # Inicializa el metodo constructor de la clase To-Do-List 
        ToDoList.contador_id += 1 #Incrementa el contador id por cada tarea añadida
        self.id = ToDoList.contador_id
        self.titulo = titulo
        self.descripcion = descripcion
        self.estado = estado
    
    # Metodo para añadir lineas separadoras
    def mostrar_linea_separadora(caracter="-", longitud=50):
        print(caracter * longitud)

    # Metodo para definir las opciones del menu principal
    def menu_opcciones():
        print("")
        opciones = [
        "",
        "1. Añadir tarea",
        "2. Mostrar tarea",
        "3. Empezar tarea",
        "4. Completar tarea",
        "5. Eliminar tarea",
        "6. Salir",
    ]
        '''Permite iterar en las opciones del menu al mismo tiempo que crea un estilo especifico'''    
        max_length = max(len(opcion) for opcion in opciones)
    
        ToDoList.mostrar_linea_separadora(longitud=max_length)
        print(Back.WHITE + Fore.BLUE + Style.BRIGHT + "  " + "= Menú Principal =  " .ljust(max_length) + Style.RESET_ALL)
        for opcion in opciones:
            print(Back.WHITE + Fore.BLACK + Style.NORMAL + "  " + opcion.ljust(max_length) + "  " + Style.RESET_ALL) 
        ToDoList.mostrar_linea_separadora(longitud=max_length)
        print("")

class ListaTareas:
    def __init__(self):
        # Inicializa la lista de tareas pendientes
        self.tareas_pendientes = []

    def añadir_tarea(self, titulo, descripcion="", estado="Pendiente"):
        # Metodo que permite añadir tareas pendientes siguiendo una estructura
        tareas = ToDoList(titulo, descripcion, estado)
        self.tareas_pendientes.append(tareas)
    
    def mostrar_tareas(self):
        ''' Muestra las tareas pendientes sin descripcion y añadiendo color dependiendo el estado rojo para pendientes, amarillo para en procesp y verde para completadas'''
        print("Lista de tareas\n")
        for tareas in self.tareas_pendientes:
            if tareas.estado == "Pendiente":
                print(Fore.RED + f"id {tareas.id}, Titulo: {tareas.titulo}, Estado: {tareas.estado}")
            elif tareas.estado == "En proceso":
                print(Fore.YELLOW + f"id {tareas.id}, Titulo: {tareas.titulo}, Estado: {tareas.estado}")
            elif tareas.estado == "Completada":
                print(Fore.GREEN + f"id {tareas.id}, Titulo: {tareas.titulo}, Estado: {tareas.estado}")

    def tarea_por_id(self,id):
        # Metodo que permite buscar de una manera efectiva por ID las tareas
        for tareas in self.tareas_pendientes:
            if tareas.id == id:
                return tareas
        return None
    
    def empezar_tarea(self, id):
        """
        Marca una tarea como 'En proceso'.
        
        Parámetros:
        id (int): El ID de la tarea a marcar como 'En proceso'.
        """
        try:
            tareas = self.tarea_por_id(id) # Busacar la tarea por ID
            if tareas:
                tareas.estado = "En proceso" # Cambia el estado de la tarea a 'En proceso'
                print(f"Tarea '{tareas.titulo}' Marcada en proceso correctamente.")
            else:
                print('ID de tarea no encontrado.')  # Si la tarea no se encuentra, se notifica
        except IndexError:
            print('posicion ingresada no valida')
    def completar_tarea(self, id):
        try:
            tareas = self.tarea_por_id(id)
            if tareas:
                tareas.estado = "Completada"
                print(f"Tarea '{tareas.titulo}' completada correctamente.")
            else:
                print('ID de tarea no encontrado.')
        except IndexError:
            print('Posición ingresada no válida')

    def eliminar_tarea(self, id):
        try:
            tarea = self.tarea_por_id(id)
            if tarea:
                verificacion = (input(f"Estas seguro que quieres borrar la tarea {id}? S/N ")).capitalize()
                if verificacion == 'S':
                    self.tareas_pendientes.remove(tarea)
                    print("Tarea eliminada correctamente.")
                elif verificacion == 'N':
                    print ("Eliminacion cancelada")
            else:
                print("Esa opcion no es valida")
        except IndexError: # Si no es correctala posicion usa la excepcion IndexError para mostrar un error
            print("El ID ingresada no es válido.")

    def ver_tarea(self, id):
        ''' Muestra los detalles de una tarea especifica'''
        tarea = self.tarea_por_id(id)
        try:
            if tarea: 
                print(f"Tarea {tarea.id}:")
                print(f"Título: {tarea.titulo}\n")
                print(f"Descripción: {tarea.descripcion}\n")
                print(f"Estado: {tarea.estado}")
                print("\nE: Empezar, C: Completar, D: Borrar, V: Volver") 
            else:
                print("ID ingresada no valida")
        except IndexError:
            print('Posición ingresada no válida')

    def opcion_tarea(self, id):
        """
        Muestra las opciones para una tarea específica.
        """
        while True:
            try:
                opcionesTarea = input("\nSeleccione una opción: ").capitalize()  # Solicita una opción
                if opcionesTarea == "V":
                    break 
                elif opcionesTarea == "D":
                    self.eliminar_tarea(id)
                    break 
                elif opcionesTarea == "E":
                    self.empezar_tarea(id)
                elif opcionesTarea == "C":
                    self.completar_tarea(id)
                else:
                    print("Opción no válida. Por favor, ingrese una opción válida: V, D, E, C.")
            except IndexError:
                print("Posición ingresada no válida")
            except ValueError:
                print("Error de valor. Por favor, ingrese una opción válida.")

def main():
    # Inicializa la lista de tareas
    listatareas = ListaTareas()
    

    while True:
        print(Fore.BLUE + Style.BRIGHT + "\n***** To-Do-List *****\n") # Titulo principal del programa
        if listatareas.tareas_pendientes: 
            listatareas.mostrar_tareas() # Visualizar las tareas pendientes, si las hay
    
        else:
            print(Style.DIM + 'No hay tareas') # Si no hay tareas avisa
        
        # Muestra el menú de opciones principal
        ToDoList.menu_opcciones()

        opcion = input("Que quieres hacer? ")

        if opcion == '1': # Añadir nueva tarea
            titulo = input("Titulo de la tarea: ")
            descripcion = input("Explica la tarea: ")
            listatareas.añadir_tarea(titulo,descripcion)
        elif opcion == "2": # Muestra una tarea especifica por ID
            id = int(input("¿Que tarea quieres ver? "))
            listatareas.ver_tarea(id)
            listatareas.opcion_tarea(id)
        elif opcion == '3': # Marca una tarea en proceso por ID
                try:
                    id = int(input("\nQue tarea quieres empezar: "))
                    listatareas.empezar_tarea(id)
                except ValueError:
                    print("Porfavor ingrese un número valido.")
        elif opcion == '4': # Marca una tarea completada por ID 
                try:
                    id = int(input("\nQue tarea esta completada? "))
                    listatareas.completar_tarea(id)
                except ValueError:
                    print("Porfavor ingrese el numero valido")

        elif opcion == '5': # Elimina una tarea por ID
            try:
                id = int(input("\nQue tarea quieres eliminar? "))
                listatareas.eliminar_tarea(id)
            except ValueError:
                print("Porfavor ingrese el numero valido")

        elif opcion == '6': # Permite salir del programa 
            salir = input("Se borrara todo el progreso ¿Seguro que quieres salir? S/N ").capitalize()
            if salir == "S":
                print("Saliendo del programa...")
                break
            elif salir == "N":
                ToDoList.menu_opcciones()
        elif opcion == "V":
            ToDoList.menu_opcciones()
    

if __name__ == "__main__":
    main()