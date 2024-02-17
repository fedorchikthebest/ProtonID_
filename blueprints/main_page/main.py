from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user
from data.db_session import db_sess
from data.services import Service

main = Blueprint('main', __name__, template_folder='templates',
                     static_folder='static', url_prefix='/main')


@main.route('/')
@login_required
def index():
    return render_template('index.html',
                           services=db_sess.query(Service).filter(Service.owner_id == current_user.id).all())


@main.errorhandler(401)
def error401(error):
    return redirect(url_for('auth.login'))