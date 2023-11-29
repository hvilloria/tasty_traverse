from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from routes import users
from models import db
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:pwd@localhost:15432/tasty_traverse_development"
app.config['SQLALCHEMY_RECORD_QUERIES'] = True
db.init_app(app)
Migrate(app, db)

app.register_blueprint(users.bp)

if __name__ == '__main__':
    with app.app_context():
        app.run(debug=True)