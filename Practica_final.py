class Tarea:
    def __init__(self, descripcion, estado="pendiente"):
        self.descripcion = descripcion
        self.estado = estado

class ListaTareas: 
    def __init__(self):
        self.tareas_pendientes = []

    def agregar_tarea(self, descripcion):
        tarea = Tarea(descripcion)
        self.tareas_pendientes.append(tarea)

    def mostrar_tareas(self):
        for i, tarea in enumerate(self.tareas_pendientes):
            if tarea.estado == "pendiente":
                print(f"{i+1}. Descripción: {tarea.descripcion}, Estado: {tarea.estado}")

    def marcar_completadas(self, posicion):
        try:
            tarea = self.tareas_pendientes[posicion]
            tarea.estado = "completada"
            print(f"Tarea '{tarea.descripcion}' marcada como completada correctamente.")
        except IndexError:
            print("La posición ingresada no es válida.")

    def eliminar_tarea(self, posicion):
        try:
            del self.tareas_pendientes[posicion]
            print("Tarea eliminada correctamente.")
        except IndexError:
            print("La posición ingresada no es válida.")

class Manual:
    def manual_tareas(self):
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
        print("\n0. Volver al menú principal")

        while True:
            try:
                opcion_manual = input("\nSeleccione una opción: ")
                if opcion_manual == '0':
                    break  # Salir del bucle y volver al menú principal
                elif opcion_manual not in ['1', '2', '3', '4', '5']:
                    raise ValueError("Opción no válida. Por favor, ingrese un número del 0 al 5.")
                else:
                    print("La opción seleccionada no está disponible en el manual. Por favor, seleccione otra opción.")
            except ValueError as e:
                print(e)

def mostrar_linea_separadora(caracter="-", longitud=50):
    print(caracter * longitud)

def mostrar_menu_principal():
    mostrar_linea_separadora()
    print("====== Menú Principal ======")
    print("\n1. Añadir nueva tarea")
    print("2. Marcar una tarea completada")
    print("3. Eliminar una tarea")
    print("4. Salir\n")
    print("5. Manual de intrucciones")
    mostrar_linea_separadora()

def mostrar_contador_tareas(num_pendientes, num_completadas):
    mostrar_linea_separadora()
    print("======= Contador de tareas =======\n")
    print(f"Tareas Pendientes: {num_pendientes}")
    print(f"Tareas Completadas: {num_completadas}")
    mostrar_linea_separadora()

def main():
    gestor = ListaTareas()
    manual = Manual()

    while True:
        mostrar_menu_principal()
        print("\n======= Lista de Tareas =======")
        num_pendientes = len(gestor.tareas_pendientes)
        num_completadas = sum(1 for tarea in gestor.tareas_pendientes if tarea.estado == "completada")

        if num_pendientes > 0:
            gestor.mostrar_tareas()
        else:
            print("\nNo hay tareas pendientes.\n")

        mostrar_contador_tareas(num_pendientes, num_completadas)

        opcion = input("\nRecuerda \n1-Añadir Tarea \n2-Completar Tareas \n3-Eliminar Tareas \nOpcion selecionada: ")

        if opcion == '1':
            descripcion = input("\nIntroduce la nueva tarea: ")
            gestor.agregar_tarea(descripcion)
        elif opcion == '2':
            if num_pendientes > 0:
                gestor.mostrar_tareas()
                try:
                    posicion = int(input("\nIngrese el número de la tarea a marcar como completada: ")) - 1
                    gestor.marcar_completadas(posicion)
                except ValueError:
                    print("Por favor, ingrese un número válido.")
            else:
                print("No hay tareas pendientes para marcar como completadas.")
        elif opcion == '3':
            if num_pendientes > 0:
                gestor.mostrar_tareas()
                try:
                    posicion = int(input("\nIngrese el número de la tarea a eliminar: ")) - 1
                    gestor.eliminar_tarea(posicion)
                except ValueError:
                    print("Por favor, ingrese un número válido.")
            else:
                print("No hay tareas pendientes para eliminar.")
        elif opcion == '4':
            print("Saliendo del programa...")
            break
        elif opcion == '5':
            manual.mostrar_manual()
            opcion_manual = input("\nSeleccione una opción: ")
            if opcion_manual == '0':
                continue  # Volver al inicio del bucle
        else:
            print("Opción no válida. Por favor, ingrese un número del 1 al 5.")

if __name__ == "__main__":
    main()