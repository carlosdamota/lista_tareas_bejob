'''Esta version ha sido completa usando ChatGpt quria ver como se implementaba la bibilioteca TKinter para mostrar el programa una interfaz de usuario'''

import tkinter as tk
from tkinter import messagebox
from colorama import init, Fore, Style

# Inicializa colorama (aunque no será útil en tkinter, se deja por si usas consola)
init(autoreset=True)

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

    def mostrar_tareas(self):
        return self.tareas_pendientes

    def empezar_tarea(self, id):
        try:
            tarea = self.tareas_pendientes[id - 1]
            tarea.estado = "En proceso"
            return f"Tarea '{tarea.titulo}' marcada en proceso correctamente."
        except IndexError:
            return 'Posición ingresada no válida'

    def completar_tarea(self, id):
        try:
            tarea = self.tareas_pendientes[id - 1]
            tarea.estado = "Completada"
            return f"Tarea '{tarea.titulo}' completada correctamente."
        except IndexError:
            return 'Posición ingresada no válida'

    def eliminar_tarea(self, id):
        try:
            del self.tareas_pendientes[id - 1]
            return "Tarea eliminada correctamente."
        except IndexError:
            return "La posición ingresada no es válida."

    def ver_tarea(self, id):
        try:
            tarea = self.tareas_pendientes[id - 1]
            return f"Tarea {tarea.id}:\nTítulo: {tarea.titulo}\nDescripción: {tarea.descripcion}\nEstado: {tarea.estado}"
        except IndexError:
            return 'Posición ingresada no válida'

class ToDoApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("To-Do List")
        self.geometry("400x400")
        self.listatareas = ListaTareas()

        self.create_widgets()

    def create_widgets(self):
        self.title_label = tk.Label(self, text="To-Do List", font=("Helvetica", 16))
        self.title_label.pack(pady=10)

        self.add_button = tk.Button(self, text="Añadir nueva tarea", command=self.add_task)
        self.add_button.pack(pady=5)

        self.view_button = tk.Button(self, text="Mostrar tareas", command=self.view_tasks)
        self.view_button.pack(pady=5)

        self.start_button = tk.Button(self, text="Empezar tarea", command=self.start_task)
        self.start_button.pack(pady=5)

        self.complete_button = tk.Button(self, text="Marcar tarea completada", command=self.complete_task)
        self.complete_button.pack(pady=5)

        self.delete_button = tk.Button(self, text="Eliminar tarea", command=self.delete_task)
        self.delete_button.pack(pady=5)

    def add_task(self):
        self.new_window(AddTaskWindow, self)

    def view_tasks(self):
        self.new_window(ViewTasksWindow, self)

    def start_task(self):
        self.new_window(StartTaskWindow, self)

    def complete_task(self):
        self.new_window(CompleteTaskWindow, self)

    def delete_task(self):
        self.new_window(DeleteTaskWindow, self)

    def new_window(self, _class, controller):
        new = tk.Toplevel(self)
        _class(new, controller)

class AddTaskWindow(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.parent = parent
        self.pack()

        self.title_label = tk.Label(self, text="Título de la tarea:")
        self.title_label.pack(pady=5)
        self.title_entry = tk.Entry(self)
        self.title_entry.pack(pady=5)

        self.description_label = tk.Label(self, text="Descripción de la tarea:")
        self.description_label.pack(pady=5)
        self.description_entry = tk.Entry(self)
        self.description_entry.pack(pady=5)

        self.add_button = tk.Button(self, text="Añadir tarea", command=self.add_task)
        self.add_button.pack(pady=5)

    def add_task(self):
        titulo = self.title_entry.get()
        descripcion = self.description_entry.get()
        self.controller.listatareas.añadir_tarea(titulo, descripcion)
        messagebox.showinfo("Info", "Tarea añadida correctamente")
        self.parent.destroy()

class ViewTasksWindow(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.pack()

        tareas = self.controller.listatareas.mostrar_tareas()
        self.tareas_listbox = tk.Listbox(self)
        self.tareas_listbox.pack(pady=10)

        for tarea in tareas:
            self.tareas_listbox.insert(tk.END, f"id {tarea.id}: {tarea.titulo} - {tarea.estado}")

        self.close_button = tk.Button(self, text="Cerrar", command=parent.destroy)
        self.close_button.pack(pady=5)

class StartTaskWindow(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.pack()

        self.id_label = tk.Label(self, text="ID de la tarea:")
        self.id_label.pack(pady=5)
        self.id_entry = tk.Entry(self)
        self.id_entry.pack(pady=5)

        self.start_button = tk.Button(self, text="Empezar tarea", command=self.start_task)
        self.start_button.pack(pady=5)

    def start_task(self):
        try:
            id = int(self.id_entry.get())
            result = self.controller.listatareas.empezar_tarea(id)
            messagebox.showinfo("Info", result)
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese un número válido")
        self.parent.destroy()

class CompleteTaskWindow(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.pack()

        self.id_label = tk.Label(self, text="ID de la tarea:")
        self.id_label.pack(pady=5)
        self.id_entry = tk.Entry(self)
        self.id_entry.pack(pady=5)

        self.complete_button = tk.Button(self, text="Completar tarea", command=self.complete_task)
        self.complete_button.pack(pady=5)

    def complete_task(self):
        try:
            id = int(self.id_entry.get())
            result = self.controller.listatareas.completar_tarea(id)
            messagebox.showinfo("Info", result)
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese un número válido")
        self.parent.destroy()

class DeleteTaskWindow(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.pack()

        self.id_label = tk.Label(self, text="ID de la tarea:")
        self.id_label.pack(pady=5)
        self.id_entry = tk.Entry(self)
        self.id_entry.pack(pady=5)

        self.delete_button = tk.Button(self, text="Eliminar tarea", command=self.delete_task)
        self.delete_button.pack(pady=5)

    def delete_task(self):
        try:
            id = int(self.id_entry.get())
            result = self.controller.listatareas.eliminar_tarea(id)
            messagebox.showinfo("Info", result)
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese un número válido")
        self.parent.destroy()

if __name__ == "__main__":
    app = ToDoApp()
    app.mainloop()