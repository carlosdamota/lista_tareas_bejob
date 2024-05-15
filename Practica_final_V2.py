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
        for tareas in enumerate(self.tareas_pendientes):
            if tareas.estado == "Pendiente":
                print(Fore.RED + f"id" {tareas.id}, Titulo: {tareas.titulo}, Estado: {tareas.estado})
            elif 
