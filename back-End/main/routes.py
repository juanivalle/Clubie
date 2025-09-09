from flask import Blueprint, render_template, redirect, url_for, request, jsonify
from flask_login import login_required
from extensions import db
from forms import RegistrationForm, EditForm, PlantForm, VentasForm
from models import User, Trazabilidad, Ventas


bp = Blueprint('main', __name__)


@bp.route('/')
@bp.route('/home.html')
def home():
    usuarios = User.query.all()
    return render_template('noLog/home.html', usuarios=usuarios)


@bp.route('/miembros.html')
@login_required
def miembros():
    form = RegistrationForm()
    usuarios = User.query.all()
    return render_template('logueado/miembros.html', form=form, users=usuarios)


@bp.route('/registerform', methods=['POST'])
@login_required
def register_user():
    form = RegistrationForm()
    if form.validate_on_submit():
        exists = User.query.filter((User.cedula == form.cedula.data) | (User.email == form.email.data)).first()
        if exists:
            return redirect(url_for('main.miembros'))
        new_user = User(
            cedula=form.cedula.data,
            name=form.name.data,
            telefono=form.telefono.data,
            email=form.email.data.lower(),
        )
        new_user.set_password(form.password.data)
        db.session.add(new_user)
        db.session.commit()
    return redirect(url_for('main.miembros'))


@bp.route('/cedula', methods=['POST'])
@login_required
def verificar_cedula():
    cedula = request.form.get('cedula', type=int)
    user = User.query.filter_by(cedula=cedula).first()
    return jsonify({'existe': user is not None})


@bp.route('/delete/<int:cedula>', methods=['POST'])
@login_required
def delete_socio(cedula: int):
    socio = User.query.get_or_404(cedula)
    db.session.delete(socio)
    db.session.commit()
    return redirect(url_for('main.miembros'))


@bp.route('/edit/<int:cedula>', methods=['GET', 'POST'])
@login_required
def editar_usuario(cedula: int):
    usuario = User.query.get_or_404(cedula)
    form = EditForm(obj=usuario)
    if form.validate_on_submit():
        usuario.cedula = form.cedula.data
        usuario.name = form.name.data
        usuario.telefono = form.telefono.data
        usuario.email = form.email.data.lower()
        db.session.commit()
        return redirect(url_for('main.miembros'))
    return render_template('logueado/edit_usuario.html', form=form, usuario=usuario)


@bp.route('/trazabilidad.html')
@login_required
def trazabilidad():
    form = PlantForm()
    return render_template('logueado/trazabilidad.html', form=form)


@bp.route('/registerplanta', methods=['POST'])
@login_required
def registerplanta():
    form = PlantForm()
    if form.validate_on_submit():
        new_planta = Trazabilidad(
            raza=form.raza.data,
            Enraizado=form.Enraizado.data,
            Riego=form.Riego.data,
            paso1=form.paso1.data,
            paso2=form.paso2.data,
            paso3=form.paso3.data,
            floracion=form.floracion.data,
            cosecha=form.cosecha.data,
            cantidad=form.cantidad.data,
            observaciones=form.observaciones.data,
        )
        db.session.add(new_planta)
        db.session.commit()
    return redirect(url_for('main.trazabilidad'))


@bp.route('/plantas')
@login_required
def ctrPlantas():
    form = PlantForm()
    planta = Trazabilidad.query.all()
    return render_template('logueado/ctrplanta.html', form=form, planta=planta)


@bp.route('/editplanta/<int:planta_id>', methods=['GET', 'POST'])
@login_required
def editar_planta(planta_id: int):
    planta = Trazabilidad.query.get_or_404(planta_id)
    form = PlantForm(obj=planta)
    if form.validate_on_submit():
        planta.raza = form.raza.data
        planta.Enraizado = form.Enraizado.data
        planta.Riego = form.Riego.data
        planta.paso1 = form.paso1.data
        planta.paso2 = form.paso2.data
        planta.paso3 = form.paso3.data
        planta.floracion = form.floracion.data
        planta.cosecha = form.cosecha.data
        planta.cantidad = form.cantidad.data
        planta.observaciones = form.observaciones.data
        db.session.commit()
        return redirect(url_for('main.ctrPlantas'))
    return render_template('logueado/edit_planta.html', form=form, planta=planta)


@bp.route('/deleteplanta/<int:planta_id>', methods=['POST'])
@login_required
def delete_planta(planta_id: int):
    elplant = Trazabilidad.query.get_or_404(planta_id)
    db.session.delete(elplant)
    db.session.commit()
    return redirect(url_for('main.ctrPlantas'))


@bp.route('/ventas')
@login_required
def ventas():
    form = VentasForm()
    # Rellenar choices con cédulas existentes
    form.cedulaVenta.choices = [(u.cedula, f"{u.cedula} - {u.name}") for u in User.query.order_by(User.cedula).all()]
    ventas = Ventas.query.all()
    return render_template('logueado/ventas.html', form=form, ventas=ventas)


@bp.route('/registerventas', methods=['POST'])
@login_required
def ventosa():
    form = VentasForm()
    form.cedulaVenta.choices = [(u.cedula, f"{u.cedula} - {u.name}") for u in User.query.order_by(User.cedula).all()]
    if form.validate_on_submit():
        new_venta = Ventas(
            user_cedula=form.cedulaVenta.data,
            raza=form.razaVenta.data,
            cantidad=form.cantVenta.data,
            retiro=form.retiro.data,
        )
        db.session.add(new_venta)
        db.session.commit()
    return redirect(url_for('main.ventas'))


@bp.route('/delete_venta/<int:venta_id>', methods=['POST'])
@login_required
def eliminar_venta(venta_id: int):
    venta = Ventas.query.get_or_404(venta_id)
    db.session.delete(venta)
    db.session.commit()
    return redirect(url_for('main.ventas'))


@bp.route('/tabla_ventas')
@login_required
def tabla_datos():
    datos = db.session.query(Ventas).all()
    return render_template('ventas.html', datos=datos)


@bp.route('/get-username')
@login_required
def get_username():
    cedula = request.args.get('cedula', type=int)
    usuario = User.query.get(cedula)
    return usuario.name if usuario else 'Usuario no encontrado'

