from flask import Flask, jsonify, render_template, request, session, redirect, url_for, abort
import psycopg2
conn = psycopg2.connect(database="demo", user="postgres",
                        password="1234", host="localhost", port=5432)

cur = conn.cursor()
cur.execute("SELECT version();")
records = cur.fetchall()

app = Flask(__name__)

app.secret_key = '528522875de1ca5ba18ec77af480e0d66a65a810b4bada578cb91f8850fba49a'


@app.route('/')
def inicio():
    if 'username' in session:
        return f'Usuario ya logueado como {session["username"]}'
    return 'No Inicio session'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('inicio'))
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('inicio'))


@app.route('/saludar/<nombre>')
def saludar(nombre):
    return f"¡Hola, {nombre}!"


@app.route('/hola')
@app.route('/saludar')
def saludogeneral():
    return "¡Hola, Usuario , como te encuentras hoy? !"


@app.route('/edad/<int:edad>')
def mostrar_edad(edad):
    return f'La edad es:{edad + 5}'


@app.route('/mostrar/<nombre>')
def mostrar(nombre):
    return render_template('mostrar.html', valor=nombre)


@app.route('/redireccion')
def redireccion():
    return redirect(url_for('saludar', nombre='Invitado'))


@app.route('/error')
def error():
    return abort(404)


@app.errorhandler(404)
def pagina_no_encontrada(error):
    return render_template('404.html', error=error), 404


@app.route('/datos/<valor>', methods=['GET', 'POST'])
def mostrar_datos(valor):
    return f'Datos recibidos: {valor} '


if __name__ == '__main__':
    app.run(debug=True)
