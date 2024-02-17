import datetime
import sqlalchemy
from .db_session import SqlAlchemyBase
from flask_login import UserMixin
from sqlalchemy import orm
from data.users import User


class Service(SqlAlchemyBase, UserMixin):
    __tablename__ = 'services'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    kuznechik_key = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    init_vector = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    owner_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id'))
    host_name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    access_type = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)

    owner = orm.relationship(User)
