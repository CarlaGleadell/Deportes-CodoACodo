from flask import Flask, render_template, request, redirect, url_for
import os
import database as db

template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
template_dir = os.path.join(template_dir, 'src', 'templates')
app = Flask(__name__, template_folder = template_dir)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/futbol')
def futbol():
    return render_template('Futbol.html')

@app.route('/voley')
def voley():
    return render_template('voley.html')

@app.route('/hockey')
def hockey():
    return render_template('hockey.html')

@app.route('/formulario')
def formulario():
    return render_template('formulario.html')


@app.route('/crear_cuenta')
def crear_cuenta():
    return render_template('crear_cuenta.html')

@app.route('/respuesta_form', methods=['POST'])
def respuesta_form():
    return render_template('respuesta_form.html') 

@app.route('/equipos')
def equipos():
    cursor = db.database.cursor()
    cursor.execute("SELECT * FROM equipos")
    resultado = cursor.fetchall()
    insertarObjetos = []
    columnas = [columna[0] for columna in cursor.description]
    for unRegistro in resultado:
        insertarObjetos.append(dict(zip(columnas, unRegistro)))
    cursor.close()
    return render_template('equipos.html', data=insertarObjetos)

@app.route('/nuevoEquipo', methods=['GET', 'POST'])
def nuevoEquipo():
    if request.method == 'POST':
        nombre = request.form['nombre']
        deporte = request.form['deporte']
        localidad = request.form['localidad']

        if nombre and deporte and localidad:
            cursor = db.database.cursor()
            sql = "INSERT INTO equipos (Nombre, Deporte, Localidad) VALUES (%s, %s, %s)"
            data = (nombre, deporte, localidad)
            cursor.execute(sql, data)
            db.database.commit()
            cursor.close()
            return redirect(url_for('equipos'))
    
    return render_template('nuevoEquipo.html')


@app.route('/modificarEquipo/<int:id>', methods=['GET', 'POST'])
def modificarEquipo(id):
    cursor = db.database.cursor(dictionary=True)  
    if request.method == 'POST':
        nombre = request.form['nombre']
        deporte = request.form['deporte']
        localidad = request.form['localidad']
        
        sql = "UPDATE equipos SET Nombre = %s, Deporte = %s, Localidad = %s WHERE Id = %s"
        data = (nombre, deporte, localidad, id)
        cursor.execute(sql, data)
        db.database.commit()
        return redirect(url_for('equipos'))
    
    cursor.execute("SELECT * FROM equipos WHERE Id = %s", (id,))
    equipo = cursor.fetchone()
    cursor.close()
    return render_template('modificarEquipo.html', equipo=equipo)

@app.route('/eliminarEquipo/<int:id>', methods=['GET', 'POST'])
def eliminarEquipo(id):
    cursor = db.database.cursor(dictionary=True)
    if request.method == 'POST':
        sql = "DELETE FROM equipos WHERE Id = %s"
        cursor.execute(sql, (id,))
        db.database.commit()
        return redirect(url_for('equipos'))
    
    cursor.execute("SELECT * FROM equipos WHERE Id = %s", (id,))
    equipo = cursor.fetchone()
    cursor.close()
    return render_template('eliminarEquipo.html', equipo=equipo)

@app.route('/jugadores/<int:equipo_id>')
def jugadores(equipo_id):
    cursor = db.database.cursor(dictionary=True)
    cursor.execute("SELECT * FROM equipos WHERE Id = %s", (equipo_id,))
    equipo = cursor.fetchone()
    cursor.execute("SELECT j.* FROM jugadores j INNER JOIN equipo_has_jugadores ej ON j.DNI = ej.jugadores_DNI WHERE ej.equipos_Id = %s", (equipo_id,))
    jugadores = cursor.fetchall()
    cursor.close()
    return render_template('jugadores.html', equipo=equipo, jugadores=jugadores)

@app.route('/nuevoJugador/<int:equipo_id>', methods=['GET', 'POST'])
def nuevoJugador(equipo_id):
    cursor = db.database.cursor(dictionary=True)
    if request.method == 'POST':
        dni = request.form['dni']
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        localidad = request.form['localidad']
        edad = request.form['edad']
        
        cursor.execute("INSERT INTO jugadores (DNI, Nombre, Apellido, Localidad, Edad) VALUES (%s, %s, %s, %s, %s)", 
                       (dni, nombre, apellido, localidad, edad))
        cursor.execute("INSERT INTO equipo_has_jugadores (jugadores_DNI, equipos_Id) VALUES (%s, %s)", 
                       (dni, equipo_id))
        db.database.commit()
        return redirect(url_for('jugadores', equipo_id=equipo_id))
    
    cursor.execute("SELECT * FROM equipos WHERE Id = %s", (equipo_id,))
    equipo = cursor.fetchone()
    cursor.close()
    return render_template('nuevoJugador.html', equipo=equipo)

@app.route('/modificarJugador/<int:dni>/<int:equipo_id>', methods=['GET', 'POST'])
def modificarJugador(dni, equipo_id):
    cursor = db.database.cursor(dictionary=True)
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        localidad = request.form['localidad']
        edad = request.form['edad']
        
        cursor.execute("UPDATE jugadores SET Nombre = %s, Apellido = %s, Localidad = %s, Edad = %s WHERE DNI = %s",
                       (nombre, apellido, localidad, edad, dni))
        db.database.commit()
        return redirect(url_for('jugadores', equipo_id=equipo_id))
    
    cursor.execute("SELECT * FROM jugadores WHERE DNI = %s", (dni,))
    jugador = cursor.fetchone()
    cursor.close()
    return render_template('modificarJugador.html', jugador=jugador, equipo_id=equipo_id)

@app.route('/eliminarJugador/<int:dni>/<int:equipo_id>', methods=['GET', 'POST'])
def eliminarJugador(dni, equipo_id):
    cursor = db.database.cursor(dictionary=True)
    if request.method == 'POST':
        cursor.execute("DELETE FROM equipo_has_jugadores WHERE jugadores_DNI = %s", (dni,))
        cursor.execute("DELETE FROM jugadores WHERE DNI = %s", (dni,))
        db.database.commit()
        return redirect(url_for('jugadores', equipo_id=equipo_id))
    
    cursor.execute("SELECT * FROM jugadores WHERE DNI = %s", (dni,))
    jugador = cursor.fetchone()
    cursor.close()
    return render_template('eliminarJugador.html', jugador=jugador, equipo_id=equipo_id)

if __name__ == '__main__':
    app.run(debug=True, port=4000)