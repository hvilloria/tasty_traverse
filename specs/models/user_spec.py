import unittest
from models.user import User
from specs import test_app as app
from models import db


class ModelsTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        db.init_app(app)

        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_user_model(self):
        user = User(username='testuser', password='passwordA1')
        with app.app_context():
            db.session.add(user)
            db.session.commit()

            user_from_db = User.query.filter_by(username='testuser').first()

        self.assertIsNotNone(user_from_db)
        self.assertEqual(user_from_db.username, 'testuser')
        self.assertEqual(user_from_db.password, 'passwordA1')

if __name__ == '__main__':
    unittest.main()
