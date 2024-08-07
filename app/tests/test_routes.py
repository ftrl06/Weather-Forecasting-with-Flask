import unittest
from app import app

class TestRoutes(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_predict(self):
        response = self.app.post('/predict', json={
            'temperature': 30,
            'humidity': 85,
            'pressure': 1012,
            'wind_speed': 5
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('prediction', response.json)

if __name__ == '__main__':
    unittest.main()
