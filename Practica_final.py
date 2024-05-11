'''Enunciado
Escribe un programa en Python utilizando Programación Orientada a Objetos que gestione
una lista de tareas pendientes. El programa deberá permitir al usuario realizar las siguientes
operaciones:
• Agregar una nueva tarea: El programa deberá permitir al usuario agregar una nueva tarea a
la lista de tareas pendientes.
• Marcar una tarea como completada: El programa deberá permitir al usuario marcar una
tarea como completada, dada su posición en la lista.
• Mostrar todas las tareas: El programa deberá imprimir en pantalla todas las tareas
pendientes, numeradas y mostrando su estado (completada o pendiente).
• Eliminar una tarea: El programa deberá permitir al usuario eliminar una tarea de la lista,
dada su posición.

El programa deberá incluir las siguientes características:
• Manejo de excepciones: El programa deberá manejar excepciones en caso de que el
usuario ingrese una opción no válida o una posición que no exista en la lista.
• Comentarios explicativos: El código deberá estar comentado para explicar su
funcionamiento en cada parte relevante.
'''
class Tarea:
    def __init__(self, descripcion, estado="pendiente"):
        self.descripcion = descripcion
        self.estado = estado

class ListaTareas: 
    #Metodo contructor de la clase ListaTareas
    def __init__(self):
        # Inicializa el atributo como una lista vacia
        self.tareas_pendientes = []

    def agregar_tarea(self, descripcion):
        # metodo para agregar nueva tarea a la lista de tareas pendientes
        tarea = Tarea(descripcion)
        # Crea una instancia de clase Tarea y la agrega a la lista de tareas_pendientes
        self.tareas_pendientes.append(tarea)

    def mostrar_tareas(self):
        '''Este método imprime en pantalla todas las tareas pendientes en la lista. Itera sobre la lista de tareas y verifica si el estado de cada tarea es "pendiente". Si lo es, imprime su descripción y estado.'''
        for i, tarea in enumerate(self.tareas_pendientes):
            if tarea.estado == "pendiente":
                print(f"{i+1}. Descripción: {tarea.descripcion}, Estado: {tarea.estado}")

    def marcar_completadas(self, posicion):
        '''Este método permite marcar una tarea como completada dada su posición en la lista. Toma como argumento la posición de la tarea que se desea marcar como completada. Intenta acceder a la tarea en la posición especificada en la lista y cambiar su estado a "completada". '''
        try:
            tarea = self.tareas_pendientes[posicion]
            tarea.estado = "completada"
            print(f"Tarea '{tarea.descripcion}' marcada como completada correctamente.")
        except IndexError:
            # Si la posición no es válida (por ejemplo, si está fuera de rango), maneja la excepción IndexError e imprime un mensaje de error.
            print("La posición ingresada no es válida.")

    def eliminar_tarea(self, posicion):
        try:
            del self.tareas_pendientes[posicion] #Eliminar la tarea de la posicion especifica de la lista
            print("Tarea eliminada correctamente.")
        except IndexError: # Si no es correctala posicion usa la excepcion IndexError para mostrar un error
            print("La posición ingresada no es válida.")

class Manual:
    
    def manual_tareas(self):
        # Metodo para mostrar el manual de instrucciones
        print("\n======== Manual de instrucciones ========")
        print("\nEste es un programa para gestionar tareas pendientes.")
        print("Se pueden realizar varias opciones como añadir tarea, completar tarea o eliminar tarea.")
        print("\nOpción 1. Añadir nueva Tarea: \nPara poder añadir una tarea, desde el menú principal tenemos que seleccionar la opción \nadecuada, en este caso corresponde al 1. Acto seguido, damos enter. \nAhora se nos pide que indiquemos la nueva tarea.")
        print("\nOpción 2. Marcar una tarea completada:\n Si seleccionamos esta opción, se abre una lista con todas las tareas pendientes para \nque seleccionemos aquella que está completada. Para continuar, tendremos que marcar el \nnúmero de la posición de la tarea seleccionada y presionar enter.")
        print("\nOpción 3. Eliminar tarea:\n Si seleccionamos esta opción, se abre una lista con todas las tareas pendientes y completadas \npara que seleccionemos aquella que queramos eliminar. Para continuar, tendremos que marcar el \nnúmero de la posición de la tarea seleccionada y presionar enter.")
        print("\nOpción 4. Salir: \nAl introducir 4 y presionar enter podremos salir de nuestro gestor de tareas.")
        print("\nEn todo momento se puede ver la cantidad de tareas pendientes y completadas, así como \nla lista de tareas pendientes.")

    def mostrar_manual(self):
        self.manual_tareas()
        print("\n0. Volver al menú principal") # Solicita una opcion

        while True:
            try:
                opcion_manual = input("\nSeleccione una opción: ") # Solicita una opcion
                if opcion_manual == '0':
                    break  # Salir del bucle y volver al menú principal
                elif opcion_manual not in ['1', '2', '3', '4', '5']: # Verifica si la opción ingresada no está en la lista de opciones válidas
                    raise ValueError("Opción no válida. Por favor, ingrese un número del 0 al 5.") # Genera una excepción ValueError si la opción no es válida
                else:
                    print("La opción seleccionada no está disponible en el manual. Por favor, seleccione otra opción.")
            except ValueError as e:
                print(e) # Imprime el mensaje de error


def mostrar_linea_separadora(caracter="-", longitud=50):
    print("")
    print(caracter * longitud)
    print("")

def mostrar_menu_principal():
    mostrar_linea_separadora()
    print("====== Menú Principal ======")
    print("\n1. Añadir nueva tarea")
    print("2. Marcar una tarea completada")
    print("3. Eliminar una tarea")
    print("4. Salir")
    print("5. Manual de intrucciones")
    mostrar_linea_separadora()

def mostrar_contador_tareas(num_pendientes, num_completadas):
    mostrar_linea_separadora()
    print("======= Contador de tareas =======\n")
    print(f"Tareas Pendientes: {num_pendientes}")
    print(f"Tareas Completadas: {num_completadas}")
    mostrar_linea_separadora()

def main():
    # Crear instancias de ListaTareas y Manual
    gestor = ListaTareas()
    manual = Manual()
    # Bucle principal para mantener el programa en ejecución
    while True:
        mostrar_menu_principal() # Mostrar el menú principal

        # Mostrar la lista de tareas y contar el número de tareas pendientes y completadas
        print("\n======= Lista de Tareas =======")
        num_pendientes = len(gestor.tareas_pendientes)
        num_completadas = sum(1 for tarea in gestor.tareas_pendientes if tarea.estado == "completada")

        if num_pendientes > 0:
            gestor.mostrar_tareas()
        else:
            print("\nNo hay tareas pendientes.")
        
        # Mostrar el contador de tareas
        mostrar_contador_tareas(num_pendientes, num_completadas)

        opcion = input("Opcion selecionada: ")
        
        # Manejar las diferentes opciones ingresadas por el usuario
        if opcion == '1': # Agregar una nueva tarea
            descripcion = input("\nIntroduce la nueva tarea: ")
            gestor.agregar_tarea(descripcion)
        elif opcion == '2': # Marcar una tarea como completada
            if num_pendientes > 0:
                gestor.mostrar_tareas()
                try:
                    posicion = int(input("\nIngrese el número de la tarea a marcar como completada: ")) - 1
                    gestor.marcar_completadas(posicion)
                except ValueError:
                    print("Por favor, ingrese un número válido.")
            else:
                print("No hay tareas pendientes para marcar como completadas.")
        elif opcion == '3': # Eliminar una tarea
            if num_pendientes > 0:
                gestor.mostrar_tareas()
                try:
                    posicion = int(input("\nIngrese el número de la tarea a eliminar: ")) - 1
                    gestor.eliminar_tarea(posicion)
                except ValueError:
                    print("Por favor, ingrese un número válido.")
            else:
                print("No hay tareas pendientes para eliminar.")
        elif opcion == '4': # Salir del programa
            print("Saliendo del programa...")
            break
        elif opcion == '5':
            manual.mostrar_manual()
            opcion_manual = input("\nSeleccione una opción: ")
            if opcion_manual == '0':
                continue  # Volver al inicio del bucle
        else:
             # Manejar la entrada inválida
            print("Opción no válida. Por favor, ingrese un número del 1 al 5.")

if __name__ == "__main__":
    main()
