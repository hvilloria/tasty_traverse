from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from routes import users
from models import db
from flask_migrate import Migrate
from os import environ
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URL')
app.config['SQLALCHEMY_RECORD_QUERIES'] = True
db.init_app(app)
Migrate(app, db)

app.register_blueprint(users.bp)

if __name__ == '__main__':
    with app.app_context():
        app.run(debug=True, host='0.0.0.0')