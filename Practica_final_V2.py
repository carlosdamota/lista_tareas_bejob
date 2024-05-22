from colorama import init, Back, Fore, Style

# Inicializa colorama
init(autoreset=True)

class ToDoList:
    contador_id = 0
    def __init__(self, titulo, descripcion="", estado="Pendiente"):
        ToDoList.contador_id += 1
        self.id = ToDoList.contador_id
        self.titulo = titulo
        self.descripcion = descripcion
        self.estado = estado
    
    def mostrar_linea_separadora(caracter="-", longitud=50):
        print("")
        print(caracter * longitud)
        print("")

    def menu_opcciones():
        opciones = [
        "",
        "1. Añadir tarea",
        "2. Mostrar tarea",
        "3. Empezar tarea",
        "4. Completar tarea",
        "5. Eliminar tarea",
        "6. Salir",
        "7. Manual de instrucciones"
    ]
    
        max_length = max(len(opcion) for opcion in opciones)
    
        ToDoList.mostrar_linea_separadora(longitud=max_length)
        print(Back.WHITE + Fore.BLUE + Style.BRIGHT + "==== Menú Principal ====".ljust(max_length) + Style.RESET_ALL)
        for opcion in opciones:
            print(Back.WHITE + Fore.BLACK + Style.NORMAL + opcion.ljust(max_length) + Style.RESET_ALL)
        ToDoList.mostrar_linea_separadora(longitud=max_length)

"""     ToDoList.mostrar_linea_separadora()
        print(Back.WHITE + Fore.BLACK + Style.BRIGHT + "==== Menú  Principal ====\n" + Style.RESET_ALL + "\n1. Añadir tarea          " + "\n2. Mostrar tarea         " + "\n3. Empezar tarea         " + "\n4. Completar Tarea       " + "\n5. Eliminar tarea        " + "\n6. Salir                 ")
        #print("\n1. Añadir tarea")
        #print("2. Mostrar tarea")
        #print("3. Empezar tarea")
        #print("4. Completar Tarea")
        #print("5. Eliminar tarea")
        #print("6. Salir")
        ToDoList.mostrar_linea_separadora()
 """
class ListaTareas:
    def __init__(self):
        self.tareas_pendientes = []

    def añadir_tarea(self, titulo, descripcion="", estado="Pendiente"):
        tareas = ToDoList(titulo, descripcion, estado)
        self.tareas_pendientes.append(tareas)
    
    def mostrar_tareas(self):
        print("Lista de tareas\n")
        for tareas in self.tareas_pendientes:
            if tareas.estado == "Pendiente":
                print(Fore.RED + f"id {tareas.id}, Titulo: {tareas.titulo}, Estado: {tareas.estado}")
            elif tareas.estado == "En proceso":
                print(Fore.YELLOW + f"id {tareas.id}, Titulo: {tareas.titulo}, Estado: {tareas.estado}")
            elif tareas.estado == "Completada":
                print(Fore.GREEN + f"id {tareas.id}, Titulo: {tareas.titulo}, Estado: {tareas.estado}")

    def tarea_por_id(self,id):
        for tareas in self.tareas_pendientes:
            if tareas.id == id:
                return tareas
        return None
    
    def empezar_tarea(self, id):
        try:
            tareas = self.tarea_por_id(id)
            if tareas:
                tareas.estado = "En proceso"
                print(f"Tarea '{tareas.titulo}' Marcada en proceso correctamente.")
        except IndexError:
            print('posicion ingresada no valida')
    def completar_tarea(self, id):
        try:
            tareas = self.tarea_por_id(id)
            if tareas:
                tareas.estado = "Completada"
                print(f"Tarea '{tareas.titulo}' completada correctamente.")
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
        while True:
            try:
                opcionesTarea = input("\nSeleccione una opción: ").capitalize()  # Solicita una opción
                if opcionesTarea == "V":
                    break
                elif opcionesTarea == "D":
                    self.empezar_tarea(id)
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
    listatareas = ListaTareas()
    

    while True:
        print(Fore.BLUE + Style.BRIGHT + "\n*** To-Do-List ***\n")
        if listatareas.tareas_pendientes:
            listatareas.mostrar_tareas()
    
        else:
            print(Style.DIM + 'No hay tareas')
        ToDoList.menu_opcciones()

        opcion = input("Que quieres hacer? ")

        if opcion == '1':
            titulo = input("Titulo de la tarea: ")
            descripcion = input("Explica la tarea: ")
            listatareas.añadir_tarea(titulo,descripcion)
        elif opcion == "2":
            id = int(input("¿Que tarea quieres ver? "))
            listatareas.ver_tarea(id)
            listatareas.opcion_tarea(id)
        elif opcion == '3':
            #if listatareas.tareas_pendientes > 0:           
                #listatareas.mostrar_tareas()
                try:
                    id = int(input("\nQue tarea quieres empezar: "))
                    listatareas.empezar_tarea(id)
                except ValueError:
                    print("Porfavor ingrese un número valido.")
        elif opcion == '4':
            #if listatareas.tareas_pendientes > 0:
                try:
                    id = int(input("\nQue tarea esta completada? "))
                    listatareas.completar_tarea(id)
                except ValueError:
                    print("Porfavor ingrese el numero valido")

        elif opcion == '5':
            #if listatareas.tareas_pendientes > 0:
            try:
                id = int(input("\nQue tarea quieres eliminar? "))
                listatareas.eliminar_tarea(id)
            except ValueError:
                print("Porfavor ingrese el numero valido")

        elif opcion == '6':
            print("Saliendo del programa...")
            break
        elif opcion == "V":
            ToDoList.menu_opcciones()
    

if __name__ == "__main__":
    main()