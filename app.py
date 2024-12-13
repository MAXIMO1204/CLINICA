# Importamos las librerías necesarias para construir nuestra aplicación.
# Flask es un framework de Python que permite crear aplicaciones web de manera sencilla.
# Incluye herramientas para manejar rutas, solicitudes HTTP y plantillas HTML.
from flask import Flask, render_template, request, redirect, session, flash, url_for  

# Estas funciones adicionales de Werkzeug se usan para manejar contraseñas de forma segura y archivos subidos.
from werkzeug.security import generate_password_hash, check_password_hash  # Para encriptar y verificar contraseñas.
from werkzeug.utils import secure_filename  # Para validar nombres de archivos subidos.

# Importamos el módulo 'os' para trabajar con operaciones relacionadas al sistema operativo, como manejar rutas de archivos.
import os  

# Función personalizada para obtener la conexión a la base de datos.
from conexion import obtener_conexion  

# mysql.connector es la librería que nos permite interactuar directamente con bases de datos MySQL desde Python.
import mysql.connector  

# Inicializamos la aplicación Flask.
# El parámetro `static_url_path` define la URL base para acceder a archivos estáticos (CSS, imágenes, etc.).
# El parámetro `static_folder` define la carpeta en la que se almacenan estos archivos estáticos.
app = Flask(__name__, static_url_path='/static', static_folder='static')  

# Definimos una clave secreta para la aplicación.
# Esta clave se utiliza para firmar datos de sesión y cookies, proporcionando mayor seguridad.
app.secret_key = 'clave_secreta_sanatorio'  

# Configuración para la carga de archivos.
# Aquí definimos la carpeta donde se guardarán los archivos que los usuarios suban.
app.config['UPLOAD_FOLDER'] = 'static/uploads'  

# Definimos las extensiones de archivo permitidas para las imágenes.
app.config['ALLOWED_EXTENSIONS'] = {'jpg', 'jpeg', 'png', 'gif'}  

# Función para verificar si un archivo tiene una extensión permitida.
def allowed_file(filename):
    """
    Verifica si un archivo tiene una extensión permitida.
    Args:
        filename (str): El nombre del archivo subido.
    Returns:
        bool: True si la extensión es válida, False en caso contrario.
    """
    # Validamos si el archivo tiene un punto en el nombre (para separar la extensión) y si esta extensión está en la lista permitida.
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


# Definimos la ruta principal de nuestra aplicación.
# Cuando un usuario accede al dominio raíz ('/'), se ejecuta esta función.
@app.route('/')
def index():
    """
    Ruta principal que renderiza la página principal.
    """
    # Renderiza un archivo HTML llamado 'principal.html' y lo muestra al usuario.
    # `render_template` busca en la carpeta `templates` de nuestro proyecto.
    return render_template('principal.html')


# Ruta para manejar el inicio de sesión.
# Este endpoint acepta solicitudes de tipo GET (mostrar el formulario) y POST (procesar los datos).
@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    Maneja el inicio de sesión de los usuarios.
    """
    # Si el método de la solicitud es POST, significa que el usuario envió el formulario.
    if request.method == 'POST':
        # Extraemos los datos ingresados por el usuario en el formulario.
        username = request.form['username']  # Nombre de usuario.
        password = request.form['password']  # Contraseña.

        try:
            # Intentamos conectarnos a la base de datos.
            conexion = obtener_conexion()
        except mysql.connector.Error as e:
            # Si ocurre un error de conexión, mostramos un mensaje y redirigimos al formulario de login.
            flash('Error al conectar a la base de datos.', 'error')  
            return redirect('/login')  

        # Si la conexión fue exitosa, buscamos al usuario en la base de datos.
        with conexion.cursor(dictionary=True) as cursor:
            cursor.execute("SELECT * FROM usuarios WHERE username = %s", (username,))  # Ejecutamos una consulta SQL.
            usuario = cursor.fetchone()  # Recuperamos el resultado de la consulta.

        conexion.close()  # Cerramos la conexión a la base de datos.

        # Si encontramos al usuario y la contraseña coincide con la almacenada en la base de datos:
        if usuario and check_password_hash(usuario['password'], password):
            # Guardamos el nombre de usuario en la sesión (esto permite que el usuario siga "logueado").
            session['username'] = username  
            flash(f"¡Bienvenido, {username}!", 'success')  # Mostramos un mensaje de éxito.
            return redirect('/dashboard')  # Redirigimos al panel principal.
        else:
            # Si el usuario o la contraseña son incorrectos, mostramos un mensaje de error.
            flash('Nombre de usuario o contraseña incorrecta.', 'error')  
            return redirect('/login')  

    # Si el método de la solicitud es GET, mostramos el formulario de login.
    return render_template('login.html')


# Ruta para manejar el registro de usuarios.
@app.route('/registro', methods=['GET', 'POST'])
def registro():
    """
    Maneja el registro de nuevos usuarios.
    """
    if request.method == 'POST':
        # Obtenemos los datos enviados por el usuario en el formulario.
        username = request.form['username']
        email = request.form['email']
        password = generate_password_hash(request.form['password'])  # Encriptamos la contraseña.

        try:
            # Intentamos conectar a la base de datos.
            conexion = obtener_conexion()
        except mysql.connector.Error as e:
            # Si ocurre un error, mostramos un mensaje y redirigimos al formulario de registro.
            flash('Error al conectar a la base de datos.', 'error')  
            return redirect('/registro')  

        try:
            # Intentamos guardar los datos del nuevo usuario en la base de datos.
            with conexion.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO usuarios (username, email, password) VALUES (%s, %s, %s)",
                    (username, email, password)
                )
                conexion.commit()  # Confirmamos los cambios en la base de datos.
                flash('Usuario registrado con éxito', 'success')  
                return redirect('/login')  
        except mysql.connector.Error as e:
            # Si ocurre un error al insertar los datos, revertimos los cambios.
            conexion.rollback()  
            flash('Error al registrar usuario.', 'error')  
            print(f"Error: {e}")  
        finally:
            # Cerramos la conexión a la base de datos.
            conexion.close()  

    # Si el método es GET, mostramos el formulario de registro.
    return render_template('registro.html')


# Ruta para cerrar sesión.
@app.route('/logout')
def logout():
    """
    Cierra la sesión del usuario actual.
    """
    session.pop('username', None)  # Eliminamos el nombre de usuario de la sesión.
    return redirect('/')  # Redirigimos al usuario a la página principal.


# Ruta para el panel principal.
@app.route('/dashboard')
def dashboard():
    """
    Muestra el panel principal del usuario, si ha iniciado sesión.
    """
    # Verificamos si el usuario ha iniciado sesión.
    if 'username' in session:  
        return redirect('/staff')  # Redirige a la página de personal.
    else:
        # Si no ha iniciado sesión, mostramos un mensaje de advertencia y redirigimos al login.
        flash('Debes iniciar sesión para acceder a esta página.', 'warning')  
        return redirect('/login')  



# Ruta para mostrar el listado del staff médico
@app.route('/staff')
def mostrar_staff():
    # Verificamos si el usuario ha iniciado sesión
    if 'username' not in session:
        flash('Debes iniciar sesión para acceder a esta página.', 'warning')
        return redirect('/login')  # Redirigimos al login si no hay sesión activa

    try:
        # Intentamos conectar a la base de datos
        conexion = obtener_conexion()
        # Usamos el bloque `with` para manejar el cursor. Esto asegura que se cierre automáticamente después de su uso.
        with conexion.cursor(dictionary=True) as cursor:
            # Ejecutamos una consulta para obtener todos los médicos
            cursor.execute("SELECT * FROM medicos")
            # Guardamos los resultados de la consulta
            medicos = cursor.fetchall()

        # Verificamos si no se encontraron médicos en la base de datos
        if not medicos:
            flash('No se encontraron médicos en la base de datos.', 'info')

        # Cerramos la conexión manualmente (aunque el `with` también lo asegura)
        conexion.close()
    except mysql.connector.Error as e:
        # Capturamos errores relacionados con MySQL
        flash('Error al conectar a la base de datos.', 'error')
        return redirect('/dashboard')  # Redirigimos al dashboard si ocurre un error

    # Renderizamos la plantilla principal pasando la lista de médicos
    return render_template('principal.html', medicos=medicos)

# Ruta para agregar un médico
@app.route('/medicos/agregar', methods=['GET', 'POST'])
def agregar_medico():
    # Verificamos si el usuario ha iniciado sesión
    if 'username' not in session:
        flash('Debes iniciar sesión para acceder a esta página.', 'warning')
        return redirect('/login')

    # Si el método de la solicitud es POST, procesamos los datos enviados
    if request.method == 'POST':
        # Obtenemos los datos del formulario
        nombre = request.form['nombre']
        especialidad = request.form['especialidad']
        dias_atencion = request.form['dias_atencion']
        foto = request.files.get('foto')  # Foto subida por el usuario

        # Inicializamos una variable para almacenar el nombre de la foto
        foto_nombre = None
        # Verificamos si se subió una foto válida
        if foto and allowed_file(foto.filename):
            # Generamos un nombre seguro para la foto
            foto_nombre = secure_filename(foto.filename)
            # Guardamos la foto en el directorio configurado
            foto.save(os.path.join(app.config['UPLOAD_FOLDER'], foto_nombre))

        try:
            # Intentamos conectar a la base de datos
            conexion = obtener_conexion()
            # Usamos `with` para manejar el cursor
            with conexion.cursor() as cursor:
                # Ejecutamos una consulta para insertar los datos del médico
                cursor.execute(
                    "INSERT INTO medicos (nombre, especialidad, dias_atencion, foto) VALUES (%s, %s, %s, %s)",
                    (nombre, especialidad, dias_atencion, foto_nombre)
                )
                # Confirmamos los cambios en la base de datos
                conexion.commit()
                flash("¡Médico agregado exitosamente!", "success")
                return redirect('/staff')  # Redirigimos al listado del staff
        except mysql.connector.Error as e:
            # Si ocurre un error, deshacemos los cambios
            conexion.rollback()
            flash(f'Error al agregar médico: {e}', 'error')
        finally:
            # Cerramos la conexión a la base de datos
            conexion.close()

    # Si el método es GET, mostramos el formulario para agregar médicos
    return render_template('agregar_medico.html')

# Ruta para editar un médico
@app.route('/medicos/editar/<int:id>', methods=['GET', 'POST'])
def editar_medico(id):
    # Verificamos si el usuario ha iniciado sesión
    if 'username' not in session:
        flash('Debes iniciar sesión para acceder a esta página.', 'warning')
        return redirect('/login')

    try:
        # Conectamos a la base de datos
        conexion = obtener_conexion()
        with conexion.cursor(dictionary=True) as cursor:
            if request.method == 'POST':
                # Obtenemos los datos enviados por el formulario
                nombre = request.form['nombre']
                especialidad = request.form['especialidad']
                dias_atencion = request.form['dias_atencion']
                foto = request.files.get('foto')

                # Procesamos la foto subida
                foto_nombre = None
                if foto and allowed_file(foto.filename):
                    foto_nombre = secure_filename(foto.filename)
                    foto.save(os.path.join(app.config['UPLOAD_FOLDER'], foto_nombre))

                if not foto_nombre:
                    # Si no se subió una nueva foto, mantenemos la foto actual
                    cursor.execute("SELECT foto FROM medicos WHERE id=%s", (id,))
                    resultado = cursor.fetchone()
                    if resultado and resultado['foto']:
                        foto_nombre = resultado['foto']

                # Actualizamos los datos del médico en la base de datos
                cursor.execute(
                    "UPDATE medicos SET nombre=%s, especialidad=%s, dias_atencion=%s, foto=%s WHERE id=%s",
                    (nombre, especialidad, dias_atencion, foto_nombre, id)
                )
                conexion.commit()
                flash("¡Médico editado exitosamente!", "success")
                return redirect('/staff')  # Redirigimos al listado del staff

            # Obtenemos los datos del médico para mostrarlos en el formulario
            cursor.execute("SELECT * FROM medicos WHERE id=%s", (id,))
            medico = cursor.fetchone()
            if not medico:
                flash("El médico solicitado no existe.", "error")
                return redirect('/staff')

    except mysql.connector.Error as e:
        # Capturamos cualquier error que ocurra al editar
        flash(f'Error al editar médico: {e}', 'error')
    finally:
        # Cerramos la conexión
        conexion.close()

    # Renderizamos la plantilla para editar médicos
    return render_template('editar_medico.html', medico=medico)

# Ruta para eliminar un médico
@app.route('/medicos/eliminar/<int:id>', methods=['POST'])
def eliminar_medico(id):
    # Verificamos si el usuario ha iniciado sesión
    if 'username' not in session:
        flash('Debes iniciar sesión para acceder a esta página.', 'warning')
        return redirect('/login')

    try:
        # Conectamos a la base de datos
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            # Ejecutamos la consulta para eliminar al médico
            cursor.execute("DELETE FROM medicos WHERE id=%s", (id,))
            conexion.commit()
            flash("¡Médico eliminado exitosamente!", "success")
    except mysql.connector.Error as e:
        # Si ocurre un error, deshacemos los cambios
        conexion.rollback()
        flash(f'Error al eliminar médico: {e}', 'error')
    finally:
        # Cerramos la conexión
        conexion.close()

    # Redirigimos al listado del staff
    return redirect('/staff')

# Ejecutamos la aplicación en modo debug para desarrollo
if __name__ == '__main__':
    app.run(debug=True)

