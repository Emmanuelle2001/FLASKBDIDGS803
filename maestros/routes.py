from flask import render_template, redirect, url_for, request, flash
from models import Maestros, db
from . import maestros
import forms


@maestros.route("/listamaes", methods={"GET","POST"})
def index():
    create_form = forms.MaestroForm(request.form)
    maestro = Maestros.query.all()
    return render_template("maestros/listadoMaestro.html", form=create_form, maestro=maestro)


@maestros.route("/nuevo", methods={"GET","POST"})
def nuevo():
    create_form = forms.MaestroForm(request.form)

    if request.method == "POST":
        maes = Maestros(
            matricula=create_form.matricula.data,
            nombre=create_form.nombre.data,
            apellidos=create_form.apellidos.data,
            especialidad=create_form.especialidad.data,
            email=create_form.email.data
        )
        db.session.add(maes)
        db.session.commit()
        return redirect(url_for("maestros.index"))

    return render_template("maestros/Maestros.html", form=create_form)


@maestros.route("/detalle", methods={"GET","POST"})
def detalle():
    if request.method == "GET":
        matricula = request.args.get("matricula")
        maes1 = db.session.query(Maestros).filter(Maestros.matricula == matricula).first()

        matricula = request.args.get("matricula")
        nombre = maes1.nombre
        apellidos = maes1.apellidos
        especialidad = maes1.especialidad
        email = maes1.email

        return render_template(
            "maestros/detalles.html",
            matricula=matricula,
            nombre=nombre,
            apellidos=apellidos,
            especialidad=especialidad,
            email=email
        )


@maestros.route("/modificar", methods={"GET","POST"})
def modificar():
    create_form = forms.MaestroForm(request.form)
    matricula = request.args.get("matricula")

    if request.method == "GET":
        maes1 = db.session.query(Maestros).filter(Maestros.matricula == matricula).first()
        create_form.matricula.data = request.args.get("matricula")
        create_form.nombre.data = maes1.nombre
        create_form.apellidos.data = maes1.apellidos
        create_form.especialidad.data = maes1.especialidad
        create_form.email.data = maes1.email

    if request.method == "POST":
        matricula = create_form.matricula.data
        maes1 = db.session.query(Maestros).filter(Maestros.matricula == matricula).first()
        maes1.matricula = create_form.matricula.data
        maes1.nombre = create_form.nombre.data
        maes1.apellidos = create_form.apellidos.data
        maes1.especialidad = create_form.especialidad.data
        maes1.email = create_form.email.data

        db.session.add(maes1)
        db.session.commit()
        return redirect(url_for("maestros.index"))

    return render_template("maestros/modificar.html", form=create_form)


@maestros.route("/eliminar", methods={"GET","POST"})
def eliminar():
    create_form = forms.MaestroForm(request.form)
    matricula = request.args.get("matricula")

    if request.method == "GET":
        maes1 = db.session.query(Maestros).filter(Maestros.matricula == matricula).first()
        create_form.matricula.data = request.args.get("matricula")
        create_form.nombre.data = maes1.nombre
        create_form.apellidos.data = maes1.apellidos
        create_form.especialidad.data = maes1.especialidad
        create_form.email.data = maes1.email

    if request.method == "POST":
        matricula = create_form.matricula.data
        maes1 = db.session.query(Maestros).filter(Maestros.matricula == matricula).first()
        db.session.delete(maes1)
        db.session.commit()
        return redirect(url_for("maestros.index"))

    return render_template("maestros/eliminar.html", form=create_form)