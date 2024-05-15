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
            tareas =self.tareas_pendientes[id]
            tareas.estado = "En proceso"
            print(f"Tarea '{tareas.titulo}' Marcada en proceso correctamente.")
        except IndexError:
            print('posicion ingresada no valida')

def main():
    listatareas = ListaTareas()

    if ToDoList.contador_id > 0:
        listatareas.mostrar_tareas()
    
    else:
        print('No hay tareas')

    
    
if __name__ == "__main__":
    main()