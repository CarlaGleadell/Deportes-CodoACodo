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

if __name__ == '__main__':
    app.run(debug=True, port=4000)