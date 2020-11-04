from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, FloatField, SelectField
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired


class ProjectForm(FlaskForm):
    project_name = StringField('Project Name:', validators=[DataRequired()])
    description = TextAreaField('Description:', validators=[DataRequired()])
    business_impact = TextAreaField('Business Impact:', validators=[DataRequired()])
    members = TextAreaField('Team Members (mail addresses):', validators=[DataRequired()])
    fte_saving = FloatField('Savings in FTEs:', validators=[DataRequired()])

    submit = SubmitField('Add')


class UpdateProject(FlaskForm):
    program_id = SelectField('Program:', coerce=int, id='select_program')
    project_name = StringField('Project Name:', validators=[DataRequired()])
    description = TextAreaField('Description:', validators=[DataRequired()])
    business_impact = TextAreaField('Business Impact:', validators=[DataRequired()])
    members = TextAreaField('Team Members:', validators=[DataRequired()])
    fte_saving = FloatField('Savings in FTEs::', validators=[DataRequired()])

    picture = FileField('Team Picture', validators=[FileAllowed(['jpg', 'png','gif','jpeg', 'svg'])])
    Update = SubmitField('Updated')


