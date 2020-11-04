from flask import render_template, Blueprint, flash, redirect, url_for, request
from flask_login import login_required
from sqlalchemy import func
from auto_shark import db
from auto_shark.models import User, Project
from auto_shark.views.admins.forms import Admin_Update_User_AccountForm

admins = Blueprint('admins', __name__)


@admins.route("/admin", methods=['GET', 'POST'])
@login_required
def index():
    users = User.query.all()
    user_count = db.session.query(User.id).count()
    projects = Project.query.all()
    product_count = db.session.query(Project.id).count()
    total_savings = db.session.query(func.sum(Project.fte_saving)).scalar()

    return render_template('admin/admin.html',
                           user_count=user_count, users=users,
                           projects=projects, product_count=product_count,
                           total_savings=total_savings,
                           )


@admins.route("/admin_delete_project/<int:id>/delete", methods=['POST'])
@login_required
def admin_delete_project(id):
    project_delete = Project.query.get_or_404(id)
    db.session.delete(project_delete)
    db.session.commit()
    flash('The Project was erased!', 'danger')
    return redirect(url_for('admins.index'))


@admins.route("/admin/user_details", methods=['GET', 'POST'])
@login_required
def user_stats():
    user_count = db.session.query(User.id).count()
    project_count = db.session.query(Project.id).count()
    user = User.query.all()
    return render_template('admin/user_detail.html', project_count=project_count,
                           user_count=user_count, user=user)


@admins.route("/admin/update_user_role/<int:id>", methods=['GET', 'POST'])
@login_required
def update_user_role(id):
    user_detail = User.query.filter_by(id=id).first_or_404()

    form = Admin_Update_User_AccountForm()
    if form.validate_on_submit():
        user_detail.fname = form.fname.data
        user_detail.email = form.email.data
        user_detail.role = form.role.data

        db.session.commit()
        flash('User Data was Updated!', 'success')
        return redirect(url_for('admins.user_stats'))
    elif request.method == 'GET':
        form.fname.data = user_detail.fname
        form.email.data = user_detail.email
        form.role.data = user_detail.role


    return render_template('admin/update_user_detail.html',
                           user_detail=user_detail, form=form,
                           )

