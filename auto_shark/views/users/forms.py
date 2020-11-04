from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, ValidationError
from auto_shark.models import User


class RegistrationForm(FlaskForm):
    fname = StringField('Name', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('email', validators=[DataRequired(), Email()])

    submit = SubmitField('Register')

    def validate_email(self, email):
        email = User.query.filter_by(email=email.data).first()
        if email:
            raise ValidationError('You Already Register, please try to log in')


class LoginForm(FlaskForm):
    email = StringField('email', validators=[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('LogIn')


class UpdateAccountForm(FlaskForm):
    email = StringField('email', validators=[DataRequired()])
    fname = StringField('Nombre Completo', validators=[DataRequired(), Length(min=2, max=20)])
    picture = FileField('Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')




