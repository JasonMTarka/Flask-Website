from flask_wtf import FlaskForm
from wtforms import SubmitField

class SudokuForm(FlaskForm):

    generate = SubmitField("Solve")
