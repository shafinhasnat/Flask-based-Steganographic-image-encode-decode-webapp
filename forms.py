from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import DataRequired, Length
from flask_wtf.file import FileField, FileRequired, FileAllowed
class encodeForm(FlaskForm):
	picture = FileField('upload image here', validators = [DataRequired(), FileAllowed(['jpg','png'])])
	text = StringField('Enter your text here', validators = [DataRequired()])
	submit = SubmitField('submit')
