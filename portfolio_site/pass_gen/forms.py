from flask_wtf import FlaskForm
from wtforms import SubmitField, BooleanField, IntegerField, StringField, validators
from wtforms.validators import DataRequired

class PassGenForm(FlaskForm):
	
	lowercase = BooleanField("Lowercase")
	uppercase = BooleanField("Uppercase")
	nums = BooleanField("Numbers")
	syms = BooleanField("Symbols")
	
	min_nums = IntegerField("Minimum Amount of Numbers", [validators.NumberRange(max=15)])
	min_syms = IntegerField("Minimum Amount of Symbols", [validators.NumberRange(max=15)])
	pass_len = IntegerField("Password Length", [validators.NumberRange(max=32)])

	display = StringField("Your Password")

	generate = SubmitField("Generate")
