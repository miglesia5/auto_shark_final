from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField, IntegerField, RadioField



class Project_Evaluation_Form(FlaskForm):
    automation_frameworks = SelectField('Points', choices=[('0', '0'), ('1', '1'), ('2', '2'),('3', '3'),('4', '4'),('5', '5')])
    kpis = SelectField('Points', choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')])
    edt = SelectField('Points', choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')])
    opensource = SelectField('Points', choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')])
    intellectual_capital = SelectField('Points', choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')])
    presentation_skills = SelectField('Points', choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')])

    submit = SubmitField('Complete Evaluation')



class Update_Project_Evaluation_Form(FlaskForm):
    automation_frameworks = SelectField('Points', choices=[('0', '0'), ('1', '1'), ('2', '2'),('3', '3'),('4', '4'),('5', '5')])
    kpis = SelectField('Points', choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')])
    edt = SelectField('Points', choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')])
    opensource = SelectField('Points', choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')])
    intellectual_capital = SelectField('Points', choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')])
    presentation_skills = SelectField('Points', choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')])

    submit = SubmitField('Complete Evaluation')


