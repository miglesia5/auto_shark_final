from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, FloatField, SelectField
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired


class NewEvaluationForm(FlaskForm):
    project = SelectField('Project:', coerce=int, id='select_category')
    submit = SubmitField('Add')


class AutomationFrameworksForm(FlaskForm):
    automation_frameworks_score = StringField('Score:', validators=[DataRequired()])
    automation_frameworks_comments = TextAreaField('Comments:', validators=[DataRequired()])
    submit = SubmitField('Add')


class KPIsForm(FlaskForm):
    kpis_score = StringField('Score:', validators=[DataRequired()])
    kpis_comments = TextAreaField('Comments:', validators=[DataRequired()])
    submit = SubmitField('Add')


class EDTForm(FlaskForm):
    edt_score = StringField('Score:', validators=[DataRequired()])
    edt_comments = TextAreaField('Comments:', validators=[DataRequired()])
    submit = SubmitField('Add')


class OpenSourceForm(FlaskForm):
    opensource_score = StringField('Score:', validators=[DataRequired()])
    opensource_comments = TextAreaField('Comments:', validators=[DataRequired()])
    submit = SubmitField('Add')
