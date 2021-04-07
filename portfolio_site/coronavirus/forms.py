from flask_wtf import FlaskForm
from wtforms import SubmitField, BooleanField, IntegerField, StringField, validators
from wtforms.validators import DataRequired

class Covid19Form(FlaskForm):

    generate = SubmitField("Scrape Data")
