from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, FloatField
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired


class ProgramForm(FlaskForm):
    program_name = StringField('Program Name:', validators=[DataRequired()])
    description = TextAreaField('Description:', validators=[DataRequired()])
    submit = SubmitField('Add')


class UpdateProgram(FlaskForm):
    program_name = StringField('Program Name:', validators=[DataRequired()])
    description = TextAreaField('Description:', validators=[DataRequired()])

    picture = FileField('Picture', validators=[FileAllowed(['jpg', 'png','gif','jpeg', 'svg'])])
    Update = SubmitField('Updated')


