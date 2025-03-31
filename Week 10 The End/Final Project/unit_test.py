import unittest
from flask import session
from main import app


class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_login(self):
        with self.app as client:
            response = client.post('/pythonlogin/', data=dict(username='testuser', password='testpassword'))
            self.assertEqual(response.status_code, 302)

            with client.session_transaction() as sess:
                self.assertTrue(sess['loggedin'])
                self.assertEqual(sess['username'], 'testuser')

    def test_register(self):
        with self.app as client:
            response = client.post('/pythonlogin/register', data=dict(username='newuser', password='newpassword', email='test@example.com'))
            self.assertEqual(response.status_code, 302)

    def test_home(self):
        with self.app as client:
            response = client.get('/')
            self.assertEqual(response.status_code, 302)

            client.post('/pythonlogin/', data=dict(username='testuser', password='testpassword'))

            response = client.get('/')
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Home Page', response.data)

    def test_profile(self):
        with self.app as client:
            response = client.get('/profile')
            self.assertEqual(response.status_code, 302)

            client.post('/pythonlogin/', data=dict(username='testuser', password='testpassword'))

            response = client.get('/profile')
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Profile Page', response.data)


if __name__ == '__main__':
    unittest.main()
