from flask_wtf import FlaskForm
from wtforms import SubmitField, BooleanField, IntegerField, StringField
from wtforms.validators import DataRequired

class SudokuForm(FlaskForm):

    generate = SubmitField("Solve")
