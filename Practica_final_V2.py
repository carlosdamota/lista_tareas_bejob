from colorama import init, Fore, Style

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
        ToDoList.mostrar_linea_separadora()
        print("====== Menú Principal ======")
        print("\n1. Añadir nueva tarea")
        print("2. Mostrar tarea")
        print("3. Marcar una tarea completada")
        print("4. Eliminar una tarea")
        print("5. Salir")
        #print("6. Manual de intrucciones")
        ToDoList.mostrar_linea_separadora()

class ListaTareas:
    def __init__(self):
        self.tareas_pendientes = []

    def añadir_tarea(self, titulo, descripcion="", estado="Pendiente"):
        tareas = ToDoList(titulo, descripcion, estado)
        self.tareas_pendientes.append(tareas)
    
    def mostrar_tareas(self):
        print("Lista de tareas")
        for tareas in self.tareas_pendientes:
            if tareas.estado == "Pendiente":
                print(Fore.RED + f"id {tareas.id}, Titulo: {tareas.titulo}, Estado: {tareas.estado}")
            elif tareas.estado == "En proceso":
                print(Fore.YELLOW + f"id {tareas.id}, Titulo: {tareas.titulo}, Estado: {tareas.estado}")
            elif tareas.estado == "Completada":
                print(Fore.GREEN + f"id {tareas.id}, Titulo: {tareas.titulo}, Estado: {tareas.estado}")
    
    def empezar_tarea(self, id):
        try:
            tareas = self.tareas_pendientes[id-1]
            tareas.estado = "En proceso"
            print(f"Tarea '{tareas.titulo}' Marcada en proceso correctamente.")
        except IndexError:
            print('posicion ingresada no valida')
    def completar_tarea(self, id):
        try:
            tarea = self.tareas_pendientes[id-1]
            tarea.estado = "Completada"
            print(f"Tarea '{tarea.titulo}' completada correctamente.")
        except IndexError:
            print('Posición ingresada no válida')

    def eliminar_tarea(self, id):
        try:
            del self.tareas_pendientes[id-1] #Eliminar la tarea de la posicion especifica de la lista
            print("Tarea eliminada correctamente.")
        except IndexError: # Si no es correctala posicion usa la excepcion IndexError para mostrar un error
            print("La posición ingresada no es válida.")

    def ver_tarea(self, id):
        try:
            tarea = self.tareas_pendientes[id-1]
            print(f"Tarea {tarea.id}:")
            print(f"Título: {tarea.titulo}")
            print(f"Descripción: {tarea.descripcion}")
            print(f"Estado: {tarea.estado}")
            print("\nE: Empezar, C: Completar, D: Borrar, V: Volver")
        except IndexError:
            print('Posición ingresada no válida')

    def opcion_tarea(self, id):
        while True:
            try:
                opcionesTarea = input("\nSeleccione una opción: ").capitalize()  # Solicita una opción
                if opcionesTarea == "V":
                    break
                elif opcionesTarea == "D":
                    del self.tareas_pendientes[id-1]
                    print("Tarea eliminada correctamente.")
                    break
                elif opcionesTarea == "E":
                    tarea = self.tareas_pendientes[id-1]
                    tarea.estado = "En proceso"
                    print(f"Tarea '{tarea.titulo}' marcada en proceso correctamente.")
                elif opcionesTarea == "C":
                    tarea = self.tareas_pendientes[id-1]
                    tarea.estado = "Completada"
                    print(f"Tarea '{tarea.titulo}' completada correctamente.")
                else:
                    print("Opción no válida. Por favor, ingrese una opción válida: V, D, E, C.")
            except IndexError:
                print("Posición ingresada no válida")
            except ValueError:
                print("Error de valor. Por favor, ingrese una opción válida.")

def main():
    listatareas = ListaTareas()
    

    while True:
        print("\nTo-Do-List\n")
        if listatareas.tareas_pendientes:
            listatareas.mostrar_tareas()
    
        else:
            print('No hay tareas')
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
        elif opcion == "V":
            ToDoList.menu_opcciones()
    

if __name__ == "__main__":
    main()