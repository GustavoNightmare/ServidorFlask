from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class CursoForm(FlaskForm):
    nombre = StringField('Nombre del Curso', validators=[
                         DataRequired(), Length(min=2, max=100)])
    instructor = StringField('Instructor', validators=[
                             DataRequired(), Length(min=2, max=100)])
    topico = StringField('Tópico', validators=[
                         DataRequired(), Length(min=2, max=100)])
    enviar = SubmitField('Enviar')
