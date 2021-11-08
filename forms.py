from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired


class TextInputForm(FlaskForm):
    text_input = StringField("Text Input", validators=[DataRequired()])
    submit = SubmitField("Submit")
