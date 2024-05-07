from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class Note(db.Model):
    __tablename__ = "notes"
    id = db.Column(db.Integer,
                   primary_key=True)
    title = db.Column(db.String(150))
    text = db.Column(db.Text)
