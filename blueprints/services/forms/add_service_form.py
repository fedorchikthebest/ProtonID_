from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, SelectField, PasswordField
from wtforms.validators import DataRequired, ValidationError, Length, Regexp


class AddServiceForm(FlaskForm):
    regex = '^((?!-))(xn--)?[a-z0-9][a-z0-9-_]{0,61}[a-z0-9]{0,1}\.(xn--)?([a-z0-9\-]{1,61}|[a-z0-9-]{1,30}\.[a-z]{2,})$'
    host = StringField('хост сервера', validators=[DataRequired(),
                                                   Regexp(regex=regex)])
    kuznechik_key = PasswordField('ключ алгоритма "кузнечик"',
                                   validators=[DataRequired(), Length(min=32, max=32,
                                                                      message="Длина ключа быть 32"),
                                               Regexp(regex='[A-Za-z]')])
    init_vec  = PasswordField('ключ алгоритма "кузнечик"',
                                   validators=[DataRequired(), Length(min=32, max=32,
                                                                      message="Длина вектора быть 8"),
                                               Regexp(regex='[A-Za-z]')])
    access_type = SelectField('Выберете тип доступа данных', choices=[(1, 'Только id'),
                                                                      (2, 'ФИО и класс учащегося')])
    submit = SubmitField('Добавить Сервис')