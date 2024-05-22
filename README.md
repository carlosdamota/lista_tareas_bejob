# Enunciado
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

## Lista de Tareas

Este proyecto es un gestor de tareas en Python que utiliza Programación Orientada a Objetos para administrar una lista de tareas pendientes.

## Funcionalidades

**Version 1.1.0**
- **Agregar una nueva tarea:** Permite al usuario agregar una nueva tarea a la lista de tareas pendientes.
- **Marcar una tarea como completada:** Permite al usuario marcar una tarea como completada, dada su posición en la lista.
- **Eliminar una tarea:** Permite al usuario eliminar una tarea de la lista, dada su posición.
- **Manejo de excepciones:** El programa maneja excepciones en caso de que el usuario ingrese una opción no válida o una posición que no exista en la lista.
- **Comentarios explicativos:** El código está comentado para explicar su funcionamiento en cada parte relevante.

**Version 2.0.0**
- **Mostrar Tarea:** Permite al usuario ver y empezar, completar o elimnar de manera unitaria una tarea de la lista.
- **Generador de ID:** Se crea un generador de ID para que pueda ser mas escalable.
- **Uso de colorama:** Se ha modificado el estilo visual, para que las tareas se vean de uno u otro color segun el estado.
- **Retirado:** He elimnado por falta de tiempo el menu en esta segunda version, asi como el poder ver la lista de tareas, ya que por defecto simpre estan visibles

## Diferencias entre el Enunciado y el Código

Función de Mostrar Todas las Tareas: Aunque el enunciado no especificaba mostrar todas las tareas, has agregado una función mostrar_todas_las_tareas que permite mostrar tanto las tareas pendientes como las completadas. Esto proporciona una visión completa del estado de todas las tareas en un solo lugar.

Separación del Menú Principal y las Tareas: En el enunciado, se pedía mostrar las tareas pendientes dentro del bucle del menú principal. Sin embargo, has separado la lógica del menú principal y la visualización de las tareas pendientes en funciones distintas (mostrar_menu_principal y mostrar_tareas_pendientes). Esto hace que el código sea más modular y fácil de entender.

Mejora de los Mensajes de Salida: Has mejorado los mensajes de salida en las funciones de marcar una tarea como completada y eliminar una tarea, proporcionando más información sobre el estado de la operación.

Además de las mejoras mencionadas anteriormente, también se ha agregado un manual y un contador de tareas que muestra el número de tareas pendientes y completadas en el menú principal. Esta característica proporciona una vista rápida y clara del estado actual de las tareas sin necesidad de revisar la lista completa. La inclusión de este contador mejora la usabilidad del programa al proporcionar información relevante de un vistazo.

**Versión 2 del Código**

En esta segunda versión del código, se han implementado varias mejoras y características adicionales. Ahora, el programa permite al usuario marcar una tarea como "En proceso", facilitando el seguimiento de las tareas que están siendo trabajadas actualmente. También se ha añadido una funcionalidad que permite ver una tarea específica con más detalle, mostrando su título, descripción y estado. Además, se han añadido opciones para empezar, completar o eliminar la tarea directamente desde la vista detallada.

La interfaz del usuario se ha mejorado significativamente utilizando la biblioteca colorama para hacerla más amigable y colorida. Los mensajes de salida y la presentación del menú principal ahora son más claros y atractivos visualmente. Además, se ha realizado un refinamiento del manejo de excepciones para cubrir más casos de errores y proporcionar mensajes de error más claros al usuario.

## Capturas de Pantalla
   ### V1 ###
![Captura menu principal](/Capturas/Practica_final_V1_3.png)
![Tareas añadidas](/Capturas/Practica_final_V1_4.png)
![Completar tareas](/Capturas/Practica_final_V1_5.png)
![Eliminar tareas](/Capturas/Practica_final_V1_6.png)
![Manual](/Capturas/Practica_final_V1_7.png)
![Mensajes de excepcion](/Capturas/Practica_final_V1_1.png)
![Mensajes de excepcion](/Capturas/Practica_final_V1_7.png)

## Cómo Ejecutar el Programa
1. Asegúrate de tener Python instalado en tu sistema.
2. Descarga el archivo `Practica_final.py`.
3. Abre una terminal y navega al directorio donde se encuentra el archivo `Practica_final.py`.
4. Ejecuta el programa con el siguiente comando:
   
   ``` bash
   python3 Practica_final.py

## Instrucciones de Uso
**Veriosion 1**
1. **Añadir nueva Tarea:**
   - Desde el menú principal (Mostrado al ejecutar el programa), seleccione la opción correspondiente al número 1.
   - Se le pedirá que ingrese la descripción de la nueva tarea y presione Enter.

2. **Marcar una tarea como completada:**
   - Desde el menú principal, seleccione la opción correspondiente al número 2.
   - Se mostrará una lista de todas las tareas pendientes.
   - Seleccione la tarea que desea marcar como completada ingresando el número de posición de la tarea y presionando Enter.

3. **Eliminar tarea:**
   - Desde el menú principal, seleccione la opción correspondiente al número 3.
   - Se mostrará una lista de todas las tareas pendientes y completadas.
   - Seleccione la tarea que desea eliminar ingresando el número de posición de la tarea y presionando Enter.

4. **Salir:**
   - Desde el menú principal, seleccione la opción correspondiente al número 4.
   - El programa se cerrará.

5. **Manual:**
   - Permite desde el menu principal selecionar el numero correspondeinte 5.
   - Aparecera el manual para gestionar la lista de tareas.
   - Para volver al menu V

# Manual de Instrucciones para el Programa de Lista de Tareas (Versión 2)

---

## Menú Principal

1. **Añadir tarea:** Permite agregar una nueva tarea. Se solicitará el título y la descripción de la tarea.
2. **Mostrar tarea:** Muestra una tarea específica ingresando su ID. Desde esta opción, se puede empezar, completar o eliminar la tarea, o volver al menú principal.
3. **Empezar tarea:** Permite marcar una tarea como "En proceso" ingresando su ID.
4. **Completar tarea:** Permite marcar una tarea como "Completada" ingresando su ID.
5. **Eliminar tarea:** Permite eliminar una tarea ingresando su ID.
6. **Salir:** Sale del programa.
7. **Manual de instrucciones:** Muestra este manual.

---

## Detalles de las Funciones

### Añadir Tarea:

- El usuario debe ingresar el título de la tarea.
- Luego, se solicita una descripción opcional.
- La tarea se agrega a la lista con el estado "Pendiente".

### Mostrar Tarea:

- El usuario ingresa el ID de la tarea.
- Se muestra el título, la descripción y el estado de la tarea.
- Opciones disponibles:
  - **E:** Empezar la tarea.
  - **C:** Completar la tarea.
  - **D:** Borrar la tarea.
  - **V:** Volver al menú principal.

### Empezar Tarea:

- El usuario ingresa el ID de la tarea que desea marcar como "En proceso".
- Se actualiza el estado de la tarea.

### Completar Tarea:

- El usuario ingresa el ID de la tarea que desea marcar como "Completada".
- Se actualiza el estado de la tarea.

### Eliminar Tarea:

- El usuario ingresa el ID de la tarea que desea eliminar.
- Se solicita confirmación antes de eliminar la tarea.

### Salir:

- Sale del programa.
## Visualización de Tareas

En todo momento, se puede ver la cantidad de tareas pendientes y completadas en el contador de tareas en la parte superior del menú principal. Además, la lista de tareas pendientes se muestra debajo del contador.

## Enlaces

- [Repositorio en GitHub](https://github.com/carlosdamota/https---github.com-carlosdamota-lista_tareas_bejob?tab=readme-ov-file)
- [Perfil de LinkedIn](https://www.linkedin.com/in/carlos-damota/)