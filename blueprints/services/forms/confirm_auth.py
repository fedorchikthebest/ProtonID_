from flask_wtf import FlaskForm
from wtforms import SubmitField, HiddenField


class ConfirmAuth(FlaskForm):
    submit = SubmitField('Войти')
    data = HiddenField('b64data')