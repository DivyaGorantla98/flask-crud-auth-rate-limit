import unittest
from src.app import create_app

class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        self.app = create_app().test_client()
    
    def test_ping(self):
        response = self.app.get("/ping")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'pong', response.data)

if __name__ == '__main__':
    unittest.main()
