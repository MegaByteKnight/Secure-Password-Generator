# tests/test_password_generator.py
import unittest
from password_generator import generate_password

class TestPasswordGenerator(unittest.TestCase):
    def test_password_length(self):
        password = generate_password(12)
        self.assertEqual(len(password), 12)

if __name__ == '__main__':
    unittest.main()
