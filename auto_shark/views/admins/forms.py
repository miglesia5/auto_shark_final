from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from auto_shark.models import User


class Admin_Update_User_AccountForm(FlaskForm):
    fname = StringField('Nombre Completo', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    role = StringField('Role', validators=[DataRequired(), Length(min=2, max=20)])

    submit = SubmitField('Update')
