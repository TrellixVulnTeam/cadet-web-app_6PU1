from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class UniformScoreSubmission(FlaskForm):
    week = StringField('Week', validators=[DataRequired()])
    score = StringField('Score', validators=[DataRequired()])
    cadet = StringField('Cadet', validators=[DataRequired()])
    submit = SubmitField('Enter Score')

class PerformanceScoreForm(FlaskForm):
    cadet = StringField('Cadet', validators=[DataRequired()])
    score = StringField('Score', validators=[DataRequired()])
    performance = StringField('Performance', validators=[DataRequired()])