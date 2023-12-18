from models import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=True, nullable=False)


    def __init__(self, username, password):
        self.username = username
        self.password = password

    def as_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'password': self.password
        }
