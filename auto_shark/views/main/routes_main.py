from flask_login import login_required
from sqlalchemy import func

from auto_shark import db
from auto_shark.models import User, Project, Module, Final, Program
from flask import render_template, Blueprint


main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
@login_required
def home():
    programs = Program.query.all()
    projects = Project.query.all()
    return render_template('main/home.html',
                           programs=programs,
                           projects=projects)


@main.route("/scores", methods=['GET', 'POST'])
@login_required
def scores():
    modules = Module.query.all()
    finals = Final.query.all()

    return render_template('main/scores.html', modules=modules, finals=finals,
                          )


@main.route("/fina_scores", methods=['GET', 'POST'])
@login_required
def final_scores():
    modules = Module.query.all()
    finals = Final.query.all()

    team_1_score = db.session.query(func.sum((Final.automation_frameworks*0.2) + (Final.kpis*0.3) + (Final.edt*0.2) + (Final.opensource*0.1) + (Final.intellectual_capital*0.1) + (Final.presentation_skills*0.1))/5).filter_by(project_name="Global Sales Portal Automation").scalar()
    team_2_score = db.session.query(func.sum((Final.automation_frameworks*0.2) + (Final.kpis*0.3) + (Final.edt*0.2) + (Final.opensource*0.1) + (Final.intellectual_capital*0.1) + (Final.presentation_skills*0.1))/5).filter_by(project_name="Dashboard - Failing Orders ").scalar()
    team_3_score = db.session.query(func.sum((Final.automation_frameworks*0.2) + (Final.kpis*0.3) + (Final.edt*0.2) + (Final.opensource*0.1) + (Final.intellectual_capital*0.1) + (Final.presentation_skills*0.1))/5).filter_by(project_name="Our New CDFA & HOLDS Tool Automation").scalar()
    team_4_score = db.session.query(func.sum((Final.automation_frameworks*0.2) + (Final.kpis*0.3) + (Final.edt*0.2) + (Final.opensource*0.1) + (Final.intellectual_capital*0.1) + (Final.presentation_skills*0.1))/5).filter_by(project_name="Power Measures in a Sec. Automation").scalar()
    team_5_score = db.session.query(func.sum((Final.automation_frameworks*0.2) + (Final.kpis*0.3) + (Final.edt*0.2) + (Final.opensource*0.1) + (Final.intellectual_capital*0.1) + (Final.presentation_skills*0.1))/5).filter_by(project_name="Supply Constraint Power Automation").scalar()
    team_6_score = db.session.query(func.sum((Final.automation_frameworks*0.2) + (Final.kpis*0.3) + (Final.edt*0.2) + (Final.opensource*0.1) + (Final.intellectual_capital*0.1) + (Final.presentation_skills*0.1))/5).filter_by(project_name="ICA and Expenses Admin Automation").scalar()
    team_7_score = db.session.query(func.sum((Final.automation_frameworks*0.2) + (Final.kpis*0.3) + (Final.edt*0.2) + (Final.opensource*0.1) + (Final.intellectual_capital*0.1) + (Final.presentation_skills*0.1))/5).filter_by(project_name="Export Accrual for TMO invoices").scalar()
    team_8_score = db.session.query(func.sum((Final.automation_frameworks*0.2) + (Final.kpis*0.3) + (Final.edt*0.2) + (Final.opensource*0.1) + (Final.intellectual_capital*0.1) + (Final.presentation_skills*0.1))/5).filter_by(project_name="Smart Operational KPI Automation").scalar()

    team_1_module = db.session.query(func.sum((Module.automation_frameworks_score) + (Module.kpis_score) + (Module.edt_score) + (Module.opensource_score))).filter_by(projectid=1).scalar()
    team_2_module = db.session.query(func.sum((Module.automation_frameworks_score) + (Module.kpis_score) + (Module.edt_score) + (Module.opensource_score))).filter_by(projectid=2).scalar()
    team_3_module = db.session.query(func.sum((Module.automation_frameworks_score) + (Module.kpis_score) + (Module.edt_score) + (Module.opensource_score))).filter_by(projectid=3).scalar()
    team_4_module = db.session.query(func.sum((Module.automation_frameworks_score) + (Module.kpis_score) + (Module.edt_score) + (Module.opensource_score))).filter_by(projectid=4).scalar()
    team_5_module = db.session.query(func.sum((Module.automation_frameworks_score) + (Module.kpis_score) + (Module.edt_score) + (Module.opensource_score))).filter_by(projectid=5).scalar()
    team_6_module = db.session.query(func.sum((Module.automation_frameworks_score) + (Module.kpis_score) + (Module.edt_score) + (Module.opensource_score))).filter_by(projectid=6).scalar()
    team_7_module = db.session.query(func.sum((Module.automation_frameworks_score) + (Module.kpis_score) + (Module.edt_score) + (Module.opensource_score))).filter_by(projectid=8).scalar()
    team_8_module = db.session.query(func.sum((Module.automation_frameworks_score) + (Module.kpis_score) + (Module.edt_score) + (Module.opensource_score))).filter_by(projectid=9).scalar()

    final_1 = (team_1_score + team_1_module)
    final_2 = (team_2_score + team_2_module)
    final_3 = (team_3_score + team_3_module)
    final_4 = (team_4_score + team_4_module)
    final_5 = (team_5_score + team_5_module)
    final_6 = (team_6_score + team_6_module)
    final_7 = (team_7_score + team_7_module)
    final_8 = (team_8_score + team_8_module)

    return render_template('main/final_scores.html', modules=modules, finals=finals,
                           final_1=final_1, final_2=final_2, final_3=final_3,
                           final_4=final_4, final_5=final_5, final_6=final_6,
                           final_7=final_7, final_8=final_8,

                           team_1_module=team_1_module, team_2_module=team_2_module,
                           team_3_module=team_3_module, team_4_module=team_4_module,
                           team_5_module=team_5_module, team_6_module=team_6_module,
                           team_7_module=team_7_module, team_8_module=team_8_module,

                           team_1_score=team_1_score, team_2_score=team_2_score,
                           team_3_score=team_3_score, team_4_score=team_4_score,
                           team_5_score=team_5_score,team_6_score=team_6_score,
                           team_7_score=team_7_score,team_8_score=team_8_score,
                           )


@main.route("/program/<program_name>")
def project_program(program_name):
    program = Program.query.filter_by(program_name=program_name).first_or_404()
    projects = Project.query.filter_by(line=program)

    return render_template('project/program_projects.html', program=program,
                           projects=projects)






