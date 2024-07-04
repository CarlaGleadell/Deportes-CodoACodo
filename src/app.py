from flask import Flask, render_template, request
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
    cursor.execute("Select * from equipos")
    resultado = cursor.fetchall()
    insertarObjetos = []
    id = [columna [0] for columna in cursor.description]
    for unRegistro in resultado:
        insertarObjetos.append(dict(zip(id, unRegistro)))
    cursor.close()

    return render_template('equipos.html', data = insertarObjetos)

@app.route('/nuevoEquipo')
def nuevoEquipo():
    return render_template('nuevoEquipo.html')

if __name__ == '__main__':
    app.run(debug=True, port=4000)