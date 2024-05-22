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

- **Agregar una nueva tarea:** Permite al usuario agregar una nueva tarea a la lista de tareas pendientes.
- **Marcar una tarea como completada:** Permite al usuario marcar una tarea como completada, dada su posición en la lista.
- **Eliminar una tarea:** Permite al usuario eliminar una tarea de la lista, dada su posición.
- **Manejo de excepciones:** El programa maneja excepciones en caso de que el usuario ingrese una opción no válida o una posición que no exista en la lista.
- **Comentarios explicativos:** El código está comentado para explicar su funcionamiento en cada parte relevante.

## Diferencias entre el Enunciado y el Código

Función de Mostrar Todas las Tareas: Aunque el enunciado no especificaba mostrar todas las tareas, has agregado una función mostrar_todas_las_tareas que permite mostrar tanto las tareas pendientes como las completadas. Esto proporciona una visión completa del estado de todas las tareas en un solo lugar.

Separación del Menú Principal y las Tareas: En el enunciado, se pedía mostrar las tareas pendientes dentro del bucle del menú principal. Sin embargo, has separado la lógica del menú principal y la visualización de las tareas pendientes en funciones distintas (mostrar_menu_principal y mostrar_tareas_pendientes). Esto hace que el código sea más modular y fácil de entender.

Mejora de los Mensajes de Salida: Has mejorado los mensajes de salida en las funciones de marcar una tarea como completada y eliminar una tarea, proporcionando más información sobre el estado de la operación.

Además de las mejoras mencionadas anteriormente, también se ha agregado un manual y un contador de tareas que muestra el número de tareas pendientes y completadas en el menú principal. Esta característica proporciona una vista rápida y clara del estado actual de las tareas sin necesidad de revisar la lista completa. La inclusión de este contador mejora la usabilidad del programa al proporcionar información relevante de un vistazo.

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

## Visualización de Tareas

En todo momento, se puede ver la cantidad de tareas pendientes y completadas en el contador de tareas en la parte superior del menú principal. Además, la lista de tareas pendientes se muestra debajo del contador.

## Enlaces

- [Repositorio en GitHub](https://github.com/carlosdamota/https---github.com-carlosdamota-lista_tareas_bejob?tab=readme-ov-file)
- [Perfil de LinkedIn](https://www.linkedin.com/in/carlos-damota/)