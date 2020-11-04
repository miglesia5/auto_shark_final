from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app

from auto_shark import db, login_manager
from flask_login import UserMixin
from sqlalchemy.orm import relationship



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(20), unique=True, nullable=False)
    role = db.Column(db.String, default='user')
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')

    module = db.relationship('Module', backref='coach', lazy=True)
    final = db.relationship('Final', backref='judge', lazy=True)

    projects = db.relationship('Project', backref='author', lazy=True)

    def __repr__(self):
        return f"{self.fname}"

class Program(db.Model):
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    program_name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100), nullable=False)

    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    projects = db.relationship('Project', backref='line', lazy=True)

    def __repr__(self):
        return f"Category('{self.category_name}')"

class Project(db.Model, UserMixin):
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)

    project_name = db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.String(250), nullable=False)
    fte_saving = db.Column(db.Integer)
    business_impact = db.Column(db.String(250), nullable=False)
    status = db.Column(db.String, default='candidate')
    members = db.Column(db.String(500))

    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')

    module = db.relationship('Module', backref='result', lazy=True)

    userid = db.Column(db.Integer, db.ForeignKey('user.id'))
    users = db.relationship(User)

    final_id = db.Column(db.Integer, db.ForeignKey('final.final_evaluation_id'), nullable=True)
    final = relationship("Final", back_populates='project_calification')

    program_id = db.Column(db.Integer, db.ForeignKey('program.id'), nullable=True)

    def __repr__(self):
        return f"{self.project_name}"


class Final(db.Model):
    __table_args__ = {'extend_existing': True}

    final_evaluation_id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    automation_frameworks= db.Column(db.Integer)
    kpis = db.Column(db.Integer)
    edt = db.Column(db.Integer)
    opensource = db.Column(db.Integer)
    intellectual_capital = db.Column(db.Integer)
    presentation_skills = db.Column(db.Integer)

    project_name = db.Column(db.String(50))
    description = db.Column(db.String(250))
    fte_saving = db.Column(db.Integer)
    business_impact = db.Column(db.String(250))
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')

    status = db.Column(db.String, default='pending')
    evaluation_date = db.Column(db.DateTime, nullable=True)

    userid = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    users = db.relationship(User)
    project_calification = db.relationship('Project', backref='calification', lazy=True)

    def __repr__(self):
        return f"Final_evaluation('{self.automation_frameworks}','{self.kpis}','{self.edt}', " \
               f"'{self.opensource}',  '{self.intelectual_capital}', '{self.presentation_skills}')"


class Module(db.Model):
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)

    automation_frameworks_score = db.Column(db.Integer, default=0)
    automation_frameworks_comments = db.Column(db.String(250))
    kpis_score = db.Column(db.Integer, default=0)
    kpis_comments = db.Column(db.String(250))
    edt_score = db.Column(db.Integer, default=0)
    edt_comments = db.Column(db.String(250))
    opensource_score = db.Column(db.Integer, default=0)
    opensource_comments = db.Column(db.String(250))
    intelectual_capital_comments = db.Column(db.String(250))
    presentation_skills_comments = db.Column(db.String(250))

    status = db.Column(db.String, default='pending')

    userid = db.Column(db.Integer, db.ForeignKey('user.id'))
    users = db.relationship(User)

    projectid = db.Column(db.Integer, db.ForeignKey('project.id'))
    projects = db.relationship(Project)

    def __repr__(self):
        return f"Module('{self.id}')"


