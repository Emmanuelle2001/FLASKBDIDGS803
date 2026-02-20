from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, IntegerField
from wtforms import validators


class UserForm(FlaskForm):

    id = IntegerField("id")

    nombre = StringField(
        "Nombre",
        [
            validators.DataRequired(message="El campo es requerido"),
            validators.Length(min=3, max=50, message="Ingrese un nombre válido")
        ]
    )

    aPaterno = StringField(
        "Apellido Paterno",
        [
            validators.DataRequired(message="El campo es requerido"),
            validators.Length(min=3, max=50, message="Ingrese un apellido válido")
        ]
    )

    email = EmailField(
        "Correo",
        [
            validators.DataRequired(message="El campo es requerido"),
            validators.Email(message="Ingrese un correo válido")
        ]
    )