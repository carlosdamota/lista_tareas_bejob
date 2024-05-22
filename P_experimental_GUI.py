'''Esta version ha sido completa usando ChatGpt quria ver como se implementaba la bibilioteca TKinter para mostrar el programa una interfaz de usuario'''
import tkinter as tk
from tkinter import simpledialog, messagebox

class ToDoList:
    contador_id = 0
    def __init__(self, titulo, descripcion="", estado="Pendiente"):
        ToDoList.contador_id += 1
        self.id = ToDoList.contador_id
        self.titulo = titulo
        self.descripcion = descripcion
        self.estado = estado

class ListaTareas:
    def __init__(self):
        self.tareas_pendientes = []

    def añadir_tarea(self, titulo, descripcion="", estado="Pendiente"):
        tarea = ToDoList(titulo, descripcion, estado)
        self.tareas_pendientes.append(tarea)
        return tarea
    
    def mostrar_tareas(self):
        tareas_pendientes = [tarea for tarea in self.tareas_pendientes if tarea.estado == "Pendiente"]
        tareas_en_proceso = [tarea for tarea in self.tareas_pendientes if tarea.estado == "En proceso"]
        tareas_completadas = [tarea for tarea in self.tareas_pendientes if tarea.estado == "Completada"]
        return tareas_pendientes, tareas_en_proceso, tareas_completadas

    def tarea_por_id(self, id):
        for tarea in self.tareas_pendientes:
            if tarea.id == id:
                return tarea
        return None
    
    def empezar_tarea(self, id):
        tarea = self.tarea_por_id(id)
        if tarea:
            tarea.estado = "En proceso"
            return True
        return False

    def completar_tarea(self, id):
        tarea = self.tarea_por_id(id)
        if tarea:
            tarea.estado = "Completada"
            return True
        return False

    def eliminar_tarea(self, id):
        tarea = self.tarea_por_id(id)
        if tarea:
            self.tareas_pendientes.remove(tarea)
            return True
        return False

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        self.listatareas = ListaTareas()

        # Frames for task lists
        self.frame_pendientes = tk.Frame(self.root)
        self.frame_proceso = tk.Frame(self.root)
        self.frame_completadas = tk.Frame(self.root)

        self.frame_pendientes.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.frame_proceso.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.frame_completadas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.label_pendientes = tk.Label(self.frame_pendientes, text="Pendientes")
        self.label_proceso = tk.Label(self.frame_proceso, text="En Proceso")
        self.label_completadas = tk.Label(self.frame_completadas, text="Completadas")

        self.label_pendientes.pack()
        self.label_proceso.pack()
        self.label_completadas.pack()

        self.listbox_pendientes = tk.Listbox(self.frame_pendientes)
        self.listbox_proceso = tk.Listbox(self.frame_proceso)
        self.listbox_completadas = tk.Listbox(self.frame_completadas)

        self.listbox_pendientes.pack(fill=tk.BOTH, expand=True)
        self.listbox_proceso.pack(fill=tk.BOTH, expand=True)
        self.listbox_completadas.pack(fill=tk.BOTH, expand=True)

        # Frame for buttons
        self.frame_buttons = tk.Frame(self.root)
        self.frame_buttons.pack(side=tk.BOTTOM, fill=tk.X)

        self.button_add = tk.Button(self.frame_buttons, text="Añadir Tarea", command=self.añadir_tarea)
        self.button_start = tk.Button(self.frame_buttons, text="Empezar Tarea", command=self.empezar_tarea)
        self.button_complete = tk.Button(self.frame_buttons, text="Completar Tarea", command=self.completar_tarea)
        self.button_delete = tk.Button(self.frame_buttons, text="Eliminar Tarea", command=self.eliminar_tarea)
        self.button_exit = tk.Button(self.frame_buttons, text="Salir", command=self.root.quit)

        buttons = [self.button_add, self.button_start, self.button_complete, self.button_delete, self.button_exit]
        for button in buttons:
            button.pack(side=tk.LEFT, fill=tk.X, expand=True)

        self.actualizar_listas()

    def actualizar_listas(self):
        self.listbox_pendientes.delete(0, tk.END)
        self.listbox_proceso.delete(0, tk.END)
        self.listbox_completadas.delete(0, tk.END)

        pendientes, en_proceso, completadas = self.listatareas.mostrar_tareas()
        for tarea in pendientes:
            self.listbox_pendientes.insert(tk.END, f"{tarea.id}: {tarea.titulo}")
        for tarea in en_proceso:
            self.listbox_proceso.insert(tk.END, f"{tarea.id}: {tarea.titulo}")
        for tarea in completadas:
            self.listbox_completadas.insert(tk.END, f"{tarea.id}: {tarea.titulo}")

    def obtener_id_seleccionado(self, listbox):
        try:
            seleccion = listbox.curselection()
            if seleccion:
                tarea_texto = listbox.get(seleccion)
                id_str = tarea_texto.split(":")[0]
                return int(id_str)
            return None
        except ValueError:
            return None

    def añadir_tarea(self):
        titulo = simpledialog.askstring("Añadir Tarea", "Título de la tarea:")
        descripcion = simpledialog.askstring("Añadir Tarea", "Descripción de la tarea:")
        if titulo:
            self.listatareas.añadir_tarea(titulo, descripcion)
            self.actualizar_listas()

    def empezar_tarea(self):
        id = self.obtener_id_seleccionado(self.listbox_pendientes)
        if id is not None:
            if self.listatareas.empezar_tarea(id):
                self.actualizar_listas()
            else:
                messagebox.showerror("Error", "ID no válida")

    def completar_tarea(self):
        id = self.obtener_id_seleccionado(self.listbox_proceso)
        if id is not None:
            if self.listatareas.completar_tarea(id):
                self.actualizar_listas()
            else:
                messagebox.showerror("Error", "ID no válida")

    def eliminar_tarea(self):
        id = self.obtener_id_seleccionado(self.listbox_pendientes) or self.obtener_id_seleccionado(self.listbox_proceso) or self.obtener_id_seleccionado(self.listbox_completadas)
        if id is not None:
            if self.listatareas.eliminar_tarea(id):
                self.actualizar_listas()
            else:
                messagebox.showerror("Error", "ID no válida")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
