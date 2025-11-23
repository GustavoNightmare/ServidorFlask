from flask import Flask, jsonify, render_template

app = Flask(__name__)


@app.route('/')
def inicio():
    return "¡Hola, Mundo desde FLASK uwu !"


@app.route('/saludar/<nombre>')
def saludar(nombre):
    return f"¡Hola, {nombre}!"


@app.route('/saludar')
def saludogeneral():
    return "¡Hola, Usuario , como te encuentras hoy? !"


@app.route('/edad/<int:edad>')
def mostrar_edad(edad):
    return f'La edad es:{edad + 5}'


@app.route('/mostrar/<nombre>')
def mostrar(nombre):
    return render_template('mostrar.html', valor=nombre)


if __name__ == '__main__':
    app.run(debug=True)
