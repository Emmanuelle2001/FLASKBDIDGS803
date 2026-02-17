from wtforms import Form
from wtforms import StringField, EmailField
from wtforms import validators


class UserForm(Form):
    id=IntergerField("id")
    nombre = StringField(
        "Nombre",
        [
            validators.DataRequired(message="El campo es requerido"),
            validators.Length(min=3, max=50, message="Ingrese un nombre válido")
        ]
    )

    apaterno = StringField(
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
