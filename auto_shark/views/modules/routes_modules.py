from flask import (render_template, url_for, flash, redirect, request, Blueprint)
from flask_login import current_user, login_required
from auto_shark import db
from auto_shark.models import Module, Project
from auto_shark.views.modules.forms import AutomationFrameworksForm, NewEvaluationForm, KPIsForm, EDTForm, \
    OpenSourceForm

modules = Blueprint('modules', __name__)


@modules.route("/module/overview", methods=['GET', 'POST'])
@login_required
def module_overview():
    modules = Module.query.all()

    return render_template('module/modules_overview.html',
                           modules=modules)


@modules.route("/module/new_evaluation", methods=['GET', 'POST'])
@login_required
def new_evaluation():
    form = NewEvaluationForm(request.form)
    projects = Project.query.all()
    form.project.choices = [(row.id, row.project_name) for row in Project.query.all()]
    if form.validate_on_submit():
        evaluation = Module(projectid=form.project.data)

        db.session.add(evaluation)
        db.session.commit()
        flash('The evaluation form for the Project chosen was created!', 'success')
        return redirect(url_for('modules.module_overview'))

    return render_template('module/new_evaluation_form.html', projects=projects,
                           form=form)


@modules.route("/delete_module/<int:id>/delete", methods=['POST'])
@login_required
def delete_module(id):
    module_delete = Module.query.get_or_404(id)
    db.session.delete(module_delete)
    db.session.commit()
    flash('The Module was erased!', 'danger')
    return redirect(url_for('modules.module_overview'))


@modules.route("/module/<int:id>/grade_automation_frameworks", methods=['GET', 'POST'])
@login_required
def grade_automation_frameworks(id):
    module = Module.query.get_or_404(id)
    form = AutomationFrameworksForm()
    if form.validate_on_submit():
        module.automation_frameworks_score = form.automation_frameworks_score.data
        module.automation_frameworks_comments = form.automation_frameworks_comments.data
        db.session.commit()
        flash('The Automation Frameworks Module for the project selected was updated!', 'success')
        return redirect(url_for('modules.module_overview', projectid=id))

    elif request.method == 'GET':
            form.automation_frameworks_score.data = module.automation_frameworks_score
            form.automation_frameworks_comments.data = module.automation_frameworks_comments
    return render_template('module/automation_framework_grade.html', form=form,
                           module=module)


@modules.route("/module/<int:id>/grade_kpis", methods=['GET', 'POST'])
@login_required
def grade_KPIs(id):
    module = Module.query.get_or_404(id)
    form = KPIsForm()
    if form.validate_on_submit():
        module.kpis_score = form.kpis_score.data
        module.kpis_comments = form.kpis_comments.data
        db.session.commit()

        flash('The Key Performances Indicators Module for the project selected was updated!', 'success')
        return redirect(url_for('modules.module_overview', projectid=id))

    elif request.method == 'GET':
            form.kpis_score.data = module.kpis_score
            form.kpis_comments.data = module.kpis_comments
    return render_template('module/kpis_grade.html', form=form,
                           module=module)


@modules.route("/module/<int:id>/grade_edt", methods=['GET', 'POST'])
@login_required
def grade_EDT(id):
    module = Module.query.get_or_404(id)
    form = EDTForm()
    if form.validate_on_submit():
        module.edt_score = form.edt_score.data
        module.edt_comments = form.edt_comments.data
        db.session.commit()

        flash('The Key Performances Indicators Module for the project selected was updated!', 'success')
        return redirect(url_for('modules.module_overview', projectid=id))

    elif request.method == 'GET':
            form.edt_score.data = module.edt_score
            form.edt_comments.data = module.edt_comments
    return render_template('module/edt_grade.html', form=form,
                           module=module)


@modules.route("/module/<int:id>/grade_opensource", methods=['GET', 'POST'])
@login_required
def grade_opensource(id):
    module = Module.query.get_or_404(id)
    form = OpenSourceForm()
    if form.validate_on_submit():
        module.opensource_score = form.opensource_score.data
        module.opensource_comments = form.opensource_comments.data
        db.session.commit()

        flash('The Key Performances Indicators Module for the project selected was updated!', 'success')
        return redirect(url_for('modules.module_overview', projectid=id))

    elif request.method == 'GET':
            form.opensource_score.data = module.opensource_score
            form.opensource_comments.data = module.opensource_comments
    return render_template('module/opensource_grade.html', form=form,
                           module=module)
