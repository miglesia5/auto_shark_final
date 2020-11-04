from flask import (render_template, url_for, flash,
                   redirect, request, Blueprint)
from flask_login import current_user, login_required
from auto_shark import db
from auto_shark.models import Program
from auto_shark.views.utils import save_picture
from auto_shark.views.programs.forms import ProgramForm, UpdateProgram

programs = Blueprint('programs', __name__)


@programs.route("/program/new", methods=['GET', 'POST'])
@login_required
def new_program():
    form = ProgramForm(request.form)
    if form.validate_on_submit():
        program = Program(program_name=form.program_name.data,
                          description=form.description.data,
                          )
        db.session.add(program)
        db.session.commit()
        flash('The Program was created!', 'success')
        return redirect(url_for('admins.index'))

    return render_template('program/new_program.html',
                           form=form)


@programs.route("/program/<int:id>/update", methods=['GET', 'POST'])
@login_required
def update_program(id):
    program = Program.query.get_or_404(id)
    form = UpdateProgram()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            program.image_file = picture_file

        program.program_name = form.program_name.data
        program.description = form.description.data
        db.session.commit()

        flash('The Program Was Updated!', 'success')
        return redirect(url_for('programs.programs_table', programid=id))

    elif request.method == 'GET':
            form.program_name.data = program.program_name
            form.description.data = program.description

    image_file = url_for('static', filename='photos/' + current_user.image_file)
    return render_template('program/update_programs.html', form=form,
                           image_file=image_file, program=program)


@programs.route("/delete_program/<int:id>/delete", methods=['POST'])
@login_required
def delete_program(id):
    program_delete = Program.query.get_or_404(id)
    db.session.delete(program_delete)
    db.session.commit()
    flash('The Program was erased!', 'danger')
    return redirect(url_for('programs.programs_table'))


@programs.route("/all_programs")
def all_projects():
        programs = Program.query.all()
        return render_template('program/all_programs.html', programs=programs)


@programs.route("/program/<int:id>")
def program(id):
    program = Program.query.get_or_404(id)
    return render_template('program/program_details.html', program=program)


@programs.route("/programs_table")
def programs_table():
        programs = Program.query.all()
        return render_template('program/programs_table.html', programs=programs)
