from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required

from auto_shark import db, bcrypt
from auto_shark.models import User, Project
from auto_shark.views.users.forms import RegistrationForm, LoginForm, UpdateAccountForm
from auto_shark.views.utils import save_picture
from auto_shark.views.projects.forms import ProjectForm

users = Blueprint('users', __name__)


@users.route("/registration", methods=['GET', 'POST'])
def registration():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(fname=form.fname.data, email=form.email.data)

        db.session.add(user)
        db.session.commit()
        flash('Your Account was create now you can LogIn', 'success')
        return redirect(url_for('users.login'))
    return render_template('users/register.html', title='Register', form=form)


@users.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.home'))
        else:
            flash('Session could not be started Please REGISTER FIRST, if any other problem please contact miglesia@mx1.ibm.com', 'danger')
    return render_template('users/login.html', title='Login', form=form)



@users.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('main.home'))


@users.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file

        current_user.fname = form.fname.data
        current_user.email = form.email.data

        db.session.commit()
        flash('Your account was updated!', 'success')
        return redirect(url_for('users.account'))
    elif request.method == 'GET':
        form.fname.data = current_user.fname
        form.email.data = current_user.email

    image_file = url_for('static', filename='photos/' + current_user.image_file)
    return render_template('users/account.html', title='Account',
                           image_file=image_file, form=form,
                           )


@users.route("/project/new", methods=['GET', 'POST'])
@login_required
def new_project():
    form = ProjectForm(request.form)
    # categories = Category.query.all() (It Can be Wave)
    # form.category.choices = [(row.id, row.category_name) for row in Category.query.all()]

    if form.validate_on_submit():
        project = Project(project_name=form.project_name.data,
                          description=form.description.data,
                          business_impact=form.business_impact.data,
                          fte_saving=form.fte_saving.data,
                          )

        db.session.add(project)
        db.session.commit()
        flash('The Project was created!', 'success')
        return redirect(url_for('main.home'))

    return render_template('project/new_project.html',
                           form=form)




###################### RESETS ####################################


@users.route("/reset_password", methods=['GET', 'POST'])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RequestResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        send_reset_email(user)
        flash('Un mail ha sido enviado con instrucciones para resetear tu cuenta', 'info')
        return redirect(url_for('users.login'))
    return render_template('users/reset_request.html', title='Reset Password', form=form)


@users.route("/reset_password/<token>", methods=['GET', 'POST'])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    user = User.verify_reset_token(token)
    if user is None:
        flash('Ese es un Token Invalido', 'warning')
        return redirect(url_for('users.reset_request'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user.password = hashed_password
        db.session.commit()
        flash('Tu Contraseña fue actualizada! Ya puede iniciar sesion', 'success')
        return redirect(url_for('users.login'))
        return render_template('users/reset_token.html', title='Reset Password', form=form)


