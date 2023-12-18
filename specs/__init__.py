from flask import Flask

test_app = Flask(__name__)
test_app.config.from_object('config.TestingConfig')
