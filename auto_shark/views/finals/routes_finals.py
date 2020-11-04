from datetime import datetime
from flask import (render_template, url_for, flash, redirect, Blueprint, request)
from flask_login import current_user, login_required
from sqlalchemy import func

from auto_shark.models import Final, Project
from auto_shark import db
from auto_shark.views.finals.forms import Project_Evaluation_Form, Update_Project_Evaluation_Form

finals = Blueprint('finals', __name__)



@finals.route("/finals_overview", methods=['GET', 'POST'])
@login_required
def finals_overview():
    projects = Project.query.all()
    finals = Final.query.filter_by(judge=current_user)

    return render_template('final/final_overview.html', finals=finals,
                           projects=projects)


@finals.route("/finals_admin_overview", methods=['GET', 'POST'])
@login_required
def finals_admin_overview():
    projects = Project.query.all()
    finals = Final.query.all()

    team_1_score = db.session.query(func.sum(
        Final.automation_frameworks + (Final.kpis) + (Final.edt) + (Final.opensource) + (Final.intellectual_capital) + (
            Final.presentation_skills))).filter_by(project_name="Global Sales Portal Automation").scalar()

    return render_template('final/final_overview.html', finals=finals,
                           projects=projects, team_1_score=team_1_score)



@finals.route("/final/int:<id>/project_form", methods=['GET', 'POST'])
@login_required
def project_form(id):
    form = Project_Evaluation_Form()
    project = Project.query.get_or_404(id)

    if form.validate_on_submit():
        add_evaluation = Final(
            automation_frameworks=form.automation_frameworks.data,
            kpis=form.kpis.data,
            edt=form.edt.data,
            opensource=form.opensource.data,
            intellectual_capital=form.intellectual_capital.data,
            presentation_skills=form.presentation_skills.data,

            project_name= project.project_name,
            description= project.description,
            fte_saving=project.fte_saving,
            business_impact=project.business_impact,
            image_file= project.image_file,

            judge=current_user)

        db.session.add(add_evaluation)
        db.session.commit()

        flash('Your Evaluation for the Selected Project has Been completed!', 'success')
        return redirect(url_for('finals.finals_overview'))

    return render_template('final/evaluation_form.html', project=project, form=form)


@finals.route("/final/int:<final_evaluation_id>/project_form_update", methods=['GET', 'POST'])
@login_required
def final(final_evaluation_id):
    project = Project.query.all()
    final = Final.query.get_or_404(final_evaluation_id)
    form = Update_Project_Evaluation_Form()
    if form.validate_on_submit():
        final.automation_frameworks = form.automation_frameworks.data
        final.kpis = form.kpis.data
        final.edt = form.edt.data
        final.opensource = form.opensource.data
        final.intellectual_capital = form.intellectual_capital.data
        final.presentation_skills = form.presentation_skills.data
        final.status = "Evaluation Complete"

        db.session.commit()

        flash('Evaluation Form was Update!', 'success')
        return redirect(url_for('finals.finals_overview'))

    elif request.method == 'GET':
        form.automation_frameworks.data = final.automation_frameworks
        form.kpis.data = final.kpis
        form.edt.data = final.edt
        form.opensource.data = final.opensource
        form.intellectual_capital.data = final.intellectual_capital
        form.presentation_skills.data = final.presentation_skills




    return render_template('final/update_evaluation_form.html',
                           project=project,
                           final=final, form=form)



@finals.route("/delete_evalaution_form/<final_evaluation_id>/delete", methods=['POST'])
@login_required
def delete_evalaution_form(final_evaluation_id):
   evalaution_form_delete = Final.query.get_or_404(final_evaluation_id)

   db.session.delete(evalaution_form_delete)
   db.session.commit()
   flash('The evaluation form was erase!', 'danger')
   return redirect(url_for('finals.finals_admin_overview'))
