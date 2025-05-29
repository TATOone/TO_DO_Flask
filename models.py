from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Tasks(db.Model):
    """ Класс таблицы tasks в базе данных """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    completed = db.Column(db.Boolean, default=False)