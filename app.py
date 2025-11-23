from flask import Flask, jsonify, render_template, request, session, redirect, url_for, abort
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped, mapped_column
from flask_migrate import Migrate

# CONEXION CON POSTGRESS CON PSYCOG2
# import psycopg2
# conn = psycopg2.connect(database="demo", user="postgres",
#                         password="1234", host="localhost", port=5432)

# cursor = conn.cursor()

# cur.execute(""" CREATE TABLE cursos(
#             curso_id SERIAL PRIMARY KEY,
#             curso_nombre VARCHAR(50) NOT NULL,
#             curso_instructor VARCHAR(50) NOT NULL,
#             curso_topico VARCHAR(100) NOT NULL);
# """)

# cursor.execute("""Insert INTO cursos
#                (curso_nombre,
#                curso_instructor,
#                 curso_topico)
#                VALUES (
#                'Fundamentod de Python',
#                'Raul Perez',
#                 'programacion'
#                );
#                """)
# cursor.execute("SELECT * FROM cursos;")
# filas = cursor.fetchall()
# conn.commit()
# cursor.close()
# conn.close()

# for fila in filas:
#     print(fila)

app = Flask(__name__)

app.secret_key = '528522875de1ca5ba18ec77af480e0d66a65a810b4bada578cb91f8850fba49a'

# Conexion a Base de Datos con SQLAlchemy y PostgreSQL

USER_DB = 'postgres'
USER_PASSWORD = '1234'
SERVER_DB = 'localhost'
NAME_DB = 'demo'

FULL_URL_DB = f'postgresql://{USER_DB}:{USER_PASSWORD}@{SERVER_DB}/{NAME_DB}'

app.config['SQLALCHEMY_DATABASE_URI'] = FULL_URL_DB

db = SQLAlchemy(app)

# Migrar el modelo

migrate = Migrate(app, db)


class Cursos(db.Model):
    __tablename__ = 'cursos'

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(
        db.String(50), unique=True, nullable=False)
    instructor: Mapped[str] = mapped_column(db.String(50), nullable=False)
    topico: Mapped[str] = mapped_column(db.String(100), nullable=False)

    def __str__(self):
        return (
            f'Curso(id={self.id}, '
            f'nombre={self.nombre}, '
            f'instructor={self.instructor}, '
            f'topico={self.topico})'
        )
# flask db init
# flask db migrate
# flask db upgrade


@app.route('/')
def inicio():
    cursos = Cursos.query.all()
    total_cursos = Cursos.query.count()
    if 'username' in session:
        return render_template('index.html', usuario=session['username'], datos=cursos, total=total_cursos)
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
