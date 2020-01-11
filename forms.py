from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import DataRequired, Length
from flask_wtf.file import FileField, FileRequired, FileAllowed
class encodeForm(FlaskForm):
	picture = FileField(validators = [DataRequired(), FileAllowed(['png'])])
	text = StringField('Enter your text:', validators = [DataRequired()])
	submit = SubmitField('submit')
