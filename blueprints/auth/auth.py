from flask import Blueprint, redirect, render_template, request, url_for
from blueprints.auth.forms.login_form import LoginForm
from flask_login import login_user, logout_user
from data.db_session import db_sess, global_init
from data.users import User
import click
import csv
import random
import string

auth = Blueprint('auth', __name__, template_folder='templates', static_folder='static', url_prefix='/auth')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = db_sess.query(User).filter(User.login == form.login.data).first()
        login_user(user, remember=form.remember_me.data)
        if request.args.get('service_id') is not None:
            return redirect(url_for("services.auth", service_id=request.args.get('service_id')))
        return redirect('/')
    return render_template('login.html', form=form)


@auth.route('/logout')
def logout():
    logout_user()
    return redirect('/')


@auth.cli.command("register-from-csv")
@click.argument("csv_file")
def register_csv(csv_file):
    if db_sess is None:
        global_init('./db/proton_id.db')
    with open(csv_file) as f:
        users = db_sess.query(User).all()
        logins = list(map(lambda n: n.login, users))
        user_data = {'logins': [], 'passwords': []}
        file = csv.DictReader(f, delimiter=';')
        for i in file:
            n = 0
            login = f"{i.get('name')}_{i.get('sure_name')}-{n}"
            while login in logins:
                n += 1
                login = f"{i.get('name')}_{i.get('sure_name')}-{n}"
            user = User(
                login=login,
                name=i.get('name'),
                sure_name=i.get('sure_name'),
                second_name=i.get('second_name'),
                class_num=i.get('class_num'),
                class_liter=i.get('class_liter'),
                is_teacher=bool(int(i.get('is_teacher')))
            )
            password = ''.join([random.choice(string.ascii_letters) for _ in range(8)])
            user.set_password(password)
            user_data['logins'].append(login)
            user_data['passwords'].append(password)
            logins.append(login)
            db_sess.add(user)
        db_sess.commit()
        with open('./users_data.csv', 'w') as w:
            fieldnames = ['login', 'password']
            writer = csv.writer(w, delimiter=';', lineterminator="\r")
            writer.writerow(fieldnames)
            writer.writerows(zip(user_data['logins'], user_data['passwords']))
        print('Логины и пароли сохранены в users_data.csv')