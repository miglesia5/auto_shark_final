from flask import (render_template, url_for, flash,
                   redirect, request, Blueprint)
from flask_login import current_user, login_required
from auto_shark import db
from auto_shark.models import Project, Program
from auto_shark.views.utils import save_picture
from auto_shark.views.projects.forms import ProjectForm, UpdateProject


projects = Blueprint('projects', __name__)


@projects.route("/project/new", methods=['GET', 'POST'])
@login_required
def new_project():
    form = ProjectForm(request.form)

    if form.validate_on_submit():
        project = Project(project_name=form.project_name.data,
                          description=form.description.data,
                          business_impact=form.business_impact.data,
                          members=form.members.data,
                          fte_saving=form.fte_saving.data,
                          )

        db.session.add(project)
        db.session.commit()
        flash('The Project was created!', 'success')
        return redirect(url_for('admins.index'))

    return render_template('project/new_project.html',
                           form=form)


@projects.route("/project/<int:id>/update", methods=['GET', 'POST'])
@login_required
def update_project(id):
    project = Project.query.get_or_404(id)
    program = Program.query.all()
    form = UpdateProject()
    form.program_id.choices = [(row.id, row.program_name) for row in Program.query.all()]
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            project.image_file = picture_file

        project.project_name = form.project_name.data
        project.description = form.description.data
        project.business_impact = form.business_impact.data
        project.members = form.members.data
        project.fte_saving = form.fte_saving.data
        project.program_id = form.program_id.data

        db.session.commit()

        flash('The Project Was Updated!', 'success')
        return redirect(url_for('admins.index', projectid=id))

    elif request.method == 'GET':
            form.project_name.data = project.project_name
            form.description.data = project.description
            form.business_impact.data = project.business_impact
            form.members.data = project.members
            form.fte_saving.data = project.fte_saving

    image_file = url_for('static', filename='photos/' + current_user.image_file)
    return render_template('project/update_project.html',
                           form=form, program=program,
                           image_file=image_file, project=project)


@projects.route("/delete_project/<int:id>/delete", methods=['POST'])
@login_required
def delete_project(id):
    project_delete = Project.query.get_or_404(id)
    db.session.delete(project_delete)
    db.session.commit()
    flash('The Project was erased!', 'danger')
    return redirect(url_for('admins.index'))


@projects.route("/all_projects")
def all_projects():
        projects = Project.query.all()
        return render_template('project/all_programs.html', projects=projects)


@projects.route("/project/<int:id>")
def project(id):
    project = Project.query.get_or_404(id)
    return render_template('project/project_details.html', project=project)


@projects.route("/move_to_participant_project/<int:id>", methods=['GET', 'POST'])
@login_required
def move_to_participant_project(id):
    project = Project.query.filter_by(id=int(id)).first()
    project.status = "Participant"

    db.session.commit()
    flash('The Project was update and move to Partipant!', 'success')
    return redirect(url_for('admins.index'))


@projects.route("/move_project_to_finalist/<int:id>", methods=['GET', 'POST'])
@login_required
def move_project_to_finalist(id):
    project = Project.query.filter_by(id=int(id)).first()
    project.status = "Finalist"

    db.session.commit()
    flash('The Project was update and move to Finalist!', 'success')
    return redirect(url_for('admins.index'))

