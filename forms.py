from flask_wtf import FlaskForm
from wtforms import SubmitField, TextField
from wtforms.validators import DataRequired


class TextInputForm(FlaskForm):
    text_input = TextField("Text Input", validators=[DataRequired()])
    submit = SubmitField("Submit")
