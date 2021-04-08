from flask_wtf import FlaskForm
from wtforms import SubmitField

class Covid19Form(FlaskForm):

    generate = SubmitField("Scrape Data")
