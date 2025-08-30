from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SubmitField
from wtforms.validators import DataRequired

class TestForm(FlaskForm):
    nombre = StringField("Nombre", validators=[DataRequired()])
    apellido = StringField("Apellido", validators=[DataRequired()])
    cumpleaños = DateField("Cumpleaños", validators=[DataRequired()], format="%Y-%m-%d")
    submit = SubmitField("Enviar")