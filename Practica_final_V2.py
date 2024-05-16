from colorama import init, Fore, Style

# Inicializa colorama
init(autoreset=True)

class ToDoList:
    contador_id = 0
    def __init__(self, titulo, descripcion="", estado="Pendiente"):
        ToDoList.contador_id += 1
        self.id = ToDoList.contador_id
        self.titulo = titulo
        self.descipcion = descripcion
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
            tareas = self.tareas_pendientes[id]
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
            del self.tareas_pendientes[id] #Eliminar la tarea de la posicion especifica de la lista
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
            print("E: Empezar, C: Completar, D: Borrar, V: Volver")
        except IndexError:
            print('Posición ingresada no válida')

    def opcion_tarea(self, id):
        while True:
            try:
                opcionesTarea = input("\nSeleccione una opción: ").capitalize # Solicita una opcion
                if opcionesTarea == "V":
                    break
                elif opcionesTarea == "D":
                    del self.tareas_pendientes[id-1]
                    break
                elif opcionesTarea == "E":
                    tareas = self.tareas_pendientes[id]
                    tareas.estado = "En proceso"
                elif opcionesTarea == "c":
                    tareas = self.tareas_pendientes[id]
                    tareas.estado = "Completada"
                elif opcionesTarea not in ['1', '2', '3', '4', '5']: # Verifica si la opción ingresada no está en la lista de opciones válidas
                    raise ValueError("Opción no válida. Por favor, ingrese un número del 0 al 5.") # Genera una excepción ValueError si la opción no es válida
                else:
                    print("La opción seleccionada no está disponible en el manual. Por favor, seleccione otra opción.")

            except IndexError:
                print("opcion introducida no valida")

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
    

if __name__ == "__main__":
    main()