TRAYECTO FORMATIVO EN PROGRAMACION



PROYECTO

CENTRO MEDICO “GRIERSON” 


Tema: PROGRAMACIÓN ORIENTADA A OBJETOS

Docente:  Prof. RODRIGO LOBO

Alumno: ATENCIO, ALBARO RAMIRO

Año: 2024

FUNDAMENTACIÓN


La programación es una herramienta fundamental para la solución de problemas en diversos sectores, incluido el ámbito de la salud. El proyecto Centro Médico 'Grierson' se desarrolla con el objetivo de modernizar la gestión de los servicios médicos mediante la creación de una aplicación web eficiente y segura.
 El uso de tecnologías avanzadas como Python y Flask permite un enfoque modular y escalable, asegurando una gestión centralizada que facilita la administración de turnos, médicos y datos de los pacientes de manera óptima y segura.
PROPOSITO DE LA INVESTIGACION

El presente proyecto se orienta a realizar una contribución en el área de metodología para el diseño, desarrollo y evaluación de software, necesarios para abordar proyectos con una metodología diferente a la estructurada.
El propósito de este proyecto es desarrollar una solución de software que permita al Centro Médico 'Grierson' ofrecer un servicio más eficiente en la gestión de turnos y personal médico. 
La implementación de un sistema web basado en Python y Flask busca automatizar procesos manuales, reducir errores, y optimizar la experiencia del usuario.




OBJETIVOS


El objetivo general de la puesta en práctica de una metodología del software es construir un producto de alta calidad de una manera oportuna. Dicha selección implica un conjunto de principios fundamentales que se deben seguir y cumplir. Estos incluyen actividades explícitas para el entendimiento del problema y la comunicación con el cliente, métodos definidos para representar un diseño, mejores prácticas para la implementación de la solución y estrategias y tácticas sólidas para las pruebas. La utilización de la metodología adecuada, representa un proceso formal que incorpora una serie de métodos bien definidos para el análisis, diseño, implementación y pruebas del software y la página web. El objetivo es contribuir al uso de metodologías modernas de desarrollo de software y proporcionar una herramienta que pueda adaptarse y escalar según las necesidades del centro médico.
•	Objetivos
1.	Desarrollar una plataforma web segura y eficiente para la gestión de médicos y turnos.
2.	Implementar una base de datos robusta para almacenar la información de usuarios, médicos y turnos.
3.	Crear un sistema de autenticación para garantizar la seguridad de los datos.
4.	Integrar una funcionalidad de manejo de archivos y documentos médicos con facilidad.
5.	Utilizar buenas prácticas de desarrollo para asegurar la calidad del código y facilitar su mantenimiento.


VENTAJAS DEL ENFOQUE PYTHON/FLASK

La migración de la solución a Python con Flask presenta múltiples ventajas, tales como:
1. Un backend sólido y escalable.
2. Mejor manejo de bases de datos gracias a integraciones con librerías como `mysql-connector`.
3.Generación dinámica de contenido mediante `Jinja2`.
4. Seguridad mejorada en el manejo de sesiones y contraseñas.


 

RESUMEN GENERAL DEL CÓDIGO
Este código Python crea una aplicación web Flask que permite gestionar un directorio de médicos. Las principales funcionalidades son:
•	Inicio de sesión y registro: Los usuarios pueden crear una cuenta y autenticarse para acceder a las funcionalidades de la aplicación.
•	Listado de médicos: Muestra una lista de todos los médicos registrados en la base de datos, incluyendo su nombre, especialidad, días de atención y foto.
•	Agregar médicos: Permite agregar nuevos médicos al sistema, incluyendo la carga de una foto.
•	Editar médicos: Permite modificar los datos de un médico existente, incluyendo la posibilidad de cambiar la foto.
•	Eliminar médicos: Permite eliminar un médico de la base de datos.
CONCEPTOS CLAVE Y FUNCIONALIDADES
•	Flask: Es el framework web de Python utilizado para construir la aplicación. Facilita la creación de rutas, manejo de solicitudes HTTP y renderizado de plantillas.
•	MySQL: Es el sistema de gestión de bases de datos utilizado para almacenar la información de los médicos.
•	Rutas: Son las diferentes URL que la aplicación puede manejar (por ejemplo, '/login', '/staff', etc.). Cada ruta está asociada a una función que se ejecuta cuando se accede a esa URL.
•	Plantillas: Son archivos HTML que contienen la estructura de las páginas web. Flask utiliza el motor de plantillas Jinja2 para renderizar estas plantillas con datos dinámicos.
•	Sesiones: Se utilizan para mantener el estado del usuario entre diferentes solicitudes. Por ejemplo, se utiliza para saber si un usuario está autenticado o no.
•	Formularios: Se utilizan para recopilar datos del usuario, como en el caso de los formularios de login, registro y edición de médicos.
•	Carga de archivos: Se utiliza para permitir a los usuarios subir archivos, en este caso, fotos de los médicos.
•	Base de datos: Se utiliza para almacenar la información de los médicos de forma persistente.



FUNCIONAMIENTO DETALLADO
•	1. Rutas y Vistas
•	¿Qué son? 
o	Las rutas son las direcciones URL que el usuario escribe en el navegador para acceder a diferentes partes de la aplicación.
o	Las vistas son las funciones Python asociadas a cada ruta, encargadas de generar la respuesta (HTML) que se enviará al usuario.
•	Ejemplo: 
@app.route('/')
def index():
    return render_template('principal.html')
o	Esta ruta '/' (la raíz de la aplicación) está asociada a la función index(). Cuando un usuario accede a la dirección principal, se ejecuta esta función y se renderiza la plantilla principal.html.

•	2. Plantillas
•	¿Qué son? 
o	Son archivos HTML que contienen la estructura de las páginas web y pueden incluir variables y lógica de control.

o	En esta plantilla, el bucle {% for medico in medicos %} itera sobre una lista de médicos y muestra su nombre y especialidad.
•	3. Base de Datos
•	¿Para qué se utiliza? 
o	Para almacenar de forma persistente la información de los médicos.
•	¿Cómo se conecta? 
o	Se utiliza el módulo mysql.connector para establecer una conexión a la base de datos y ejecutar consultas SQL.


•	Ejemplo: 
with conexion.cursor() as cursor:
    cursor.execute("SELECT * FROM medicos")
    medicos = cursor.fetchall()
o	Este código ejecuta una consulta SQL para obtener todos los médicos de la base de datos y almacena los resultados en la variable medicos.
•	4. Formularios
¿Qué es CRUD en el contexto de formularios?
CRUD es un acrónimo que representa las cuatro operaciones básicas que se realizan sobre los datos:
•	Create (Crear): Agregar un nuevo registro (por ejemplo, un nuevo médico).
•	Read (Leer): Mostrar la información existente (por ejemplo, la lista de todos los médicos).
•	Update (Actualizar): Modificar un registro existente (por ejemplo, editar los datos de un médico).
•	Delete (Eliminar): Borrar un registro (por ejemplo, eliminar un médico).
Cómo funciona el CRUD en el código:
1.	Creación de un formulario:
o	Se utiliza HTML para crear un formulario con campos para los datos que se desean capturar (nombre, especialidad, etc.).
o	Los datos ingresados por el usuario en el formulario se envían al servidor mediante el método HTTP POST.
2.	Procesamiento del formulario:
o	Cuando el servidor recibe una solicitud POST, se ejecuta la función asociada a la ruta del formulario.
o	Los datos enviados en el formulario se extraen de request.form.
o	Se valida la información para asegurarse de que sea correcta y completa.
o	Se ejecuta una consulta SQL para insertar los datos en la base de datos.
3.	Lectura de datos:
o	Se ejecutan consultas SQL para obtener los datos de la base de datos y mostrarlos en una página web.
o	Por ejemplo, para mostrar la lista de todos los médicos, se ejecuta una consulta SELECT * FROM medicos.
4.	Actualización de datos:
o	Se muestra un formulario prellenado con los datos del registro que se desea modificar.
o	Cuando se envía el formulario, se actualiza el registro correspondiente en la base de datos.
5.	Eliminación de datos:
o	Se confirma al usuario que desea eliminar el registro.
o	Se ejecuta una consulta SQL para eliminar el registro de la base de datos.




Ejemplo práctico: Agregar un nuevo médico
@app.route('/medicos/agregar', methods=['GET', 'POST'])
def agregar_medico():
    if request.method == 'POST':
        nombre = request.form['nombre']
        especialidad = request.form['especialidad']
        # ... otros datos

        # Insertar en la base de datos
        with conexion.cursor() as cursor:
            cursor.execute("INSERT INTO medicos (nombre, especialidad, ...) VALUES (%s, %s, ...)", 
                           (nombre, especialidad, ...))
            conexion.commit()
        return redirect('/staff')
    # ... (código para mostrar el formulario)
Explicación:
•	request.method == 'POST': Verifica si el formulario fue enviado (método HTTP POST).
•	request.form['nombre']: Obtiene el valor del campo "nombre" del formulario.
•	INSERT INTO: Inserta un nuevo registro en la tabla "medicos".
•	conexion.commit(): Confirma los cambios en la base de datos.
Los formularios son la interfaz entre el usuario y la aplicación, permitiendo la entrada de datos. El código del servidor procesa estos datos, interactúa con la base de datos y actualiza la interfaz de usuario en consecuencia. El patrón CRUD proporciona una estructura clara para realizar las operaciones más comunes sobre los datos.
•	5. Sesiones
•	¿Para qué se utilizan? 
o	Para mantener el estado del usuario entre diferentes solicitudes. Por ejemplo, para saber si un usuario está autenticado.
•	Ejemplo: 
session['username'] = username
o	Este código almacena el nombre de usuario del usuario en la sesión, lo que permite identificarlo en futuras solicitudes.
•	6. Carga de Archivos
•	¿Para qué se utiliza? 
o	Para permitir a los usuarios subir archivos, como fotos de perfil.
•	¿Cómo se realiza? 
o	Se utiliza request.files para acceder a los archivos subidos y se guardan en un directorio específico.



CONCEPTOS ADICIONALES
•	MVC: El patrón Modelo-Vista-Controlador se utiliza para organizar la aplicación. El modelo representa los datos (base de datos), la vista es la interfaz de usuario (plantillas) y el controlador gestiona las solicitudes y las respuestas.
•	Werkzeug: Es una biblioteca de Python que proporciona herramientas para crear aplicaciones web, como la generación de hashes de contraseñas y la validación de archivos.

PUNTOS CLAVE A DESTACAR
•	Seguridad: Se utiliza encriptación para proteger las contraseñas de los usuarios.
•	Validación de datos: Se valida que los datos ingresados por el usuario sean correctos y seguros.
•	Manejo de errores: Se incluyen bloques try-except para manejar posibles errores que puedan ocurrir durante la ejecución de la aplicación.
•	Modularidad: El código está organizado en funciones y rutas, lo que facilita la lectura y el mantenimiento.

