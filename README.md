# Description

### The code is a Python socket client that connects to a remote server to obtain temperature and humidity data. The client is responsible for verifying and installing the necessary libraries, obtaining the server's IP address through the control_configuracion() function, and allowing the user to select different options to request information from the server.  
<br>

### The general flow of the client code is as follows:

<br>

1. The necessary libraries are imported, such as os, socket, rich, ast, rich.table, colorama, and datetime.

2. The verify_installation_libraries() function is defined to verify and install the necessary libraries.

3. The control_configuracion() function is defined to obtain the server's IP address through an interactive menu.

4. The mensajecontrol() function is defined to obtain the user's option to request information from the server.

5. The socket connection to the remote server is established using the specified IP address and port.

6. The welcome message from the server is received and displayed.

7. An interactive menu is displayed for the user to select different options to request information from the server.

8. The user's selected message is sent to the server, and the server's response is received.

9. Depending on the option selected by the user, the temperature and humidity information is updated in a local dictionary dict_data_local.

10. If the user selects option 4, the main loop is exited, and the connection with the server is closed.
  

<br><br>

# Descripción

### El código es un cliente de socket en Python que se conecta a un servidor remoto para obtener datos de temperatura y humedad. El cliente se encarga de verificar e instalar las librerías necesarias, obtener la dirección IP del servidor a través de la función control_configuracion(), y permite al usuario seleccionar diferentes opciones para solicitar información al servidor.

<br>

### El flujo general del código del cliente es el siguiente:

<br>

1. Se importan las librerías necesarias, como os, socket, rich, ast, rich.table, colorama y datetime.

2. Se define la función verificar_instalacion_librerias() para verificar e instalar las librerías necesarias.

3. Se define la función control_configuracion() para obtener la dirección IP del servidor a través de un menú interactivo.

4. Se define la función mensajecontrol() para obtener la opción del usuario para solicitar información al servidor.

5. Se establece la conexión del socket con el servidor remoto a través de la dirección IP y el puerto especificados.

6. Se recibe y se muestra el mensaje de bienvenida del servidor.

7. Se muestra un menú interactivo para que el usuario seleccione diferentes opciones para solicitar información al servidor.

8. Se envía el mensaje seleccionado por el usuario al servidor y se recibe la respuesta del servidor.

9. Dependiendo de la opción seleccionada por el usuario, se actualiza la información de temperatura y humedad en un diccionario local dict_data_local.

10. Si el usuario selecciona la opción 4, se sale del bucle principal y se cierra la conexión con el servidor.
