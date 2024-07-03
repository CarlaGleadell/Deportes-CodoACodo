from flask import Flask
from flask import Flask, render_template
import os
import database as db

template_dir=os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
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

@app.route('/equipos')
def equipos():
    return render_template('equipos.html')

if __name__ == '__main__':
    app.run(debug=True, port=4000)

