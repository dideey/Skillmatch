import unittest
from werkzeug.security import generate_password_hash

class TestPasswordHashing(unittest.TestCase):
    def test_generate_password_hash(self):
        # Test with a known password
        password = "password123"
        hashed_password = generate_password_hash(password)
        
        # Ensure the hashed password is not equal to the original password
        self.assertNotEqual(hashed_password, password)
        
        # Test with another known password
        another_password = "securepassword"
        another_hashed_password = generate_password_hash(another_password)
        
        # Ensure the hashed password is not equal to the original password
        self.assertNotEqual(another_hashed_password, another_password)

        # You can add more test cases as needed

if __name__ == '__main__':
    unittest.main()
