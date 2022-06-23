# project/models.py

# Docs: https://flask-sqlalchemy.palletsprojects.com/en/2.x/

from project import db

class Adres(db.Model):

    __tablename__ = 'adressen'

    adres_id = db.Column(db.Integer, primary_key=True)
    naam = db.Column(db.String, nullable=False)
    adres = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'<naam: {self.naam}>'