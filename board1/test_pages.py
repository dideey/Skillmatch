import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

import unittest
from flask import Flask, request
from flask_testing import TestCase
from pages import signup_post

from board1 import create_app, db

class PagesTestCase(TestCase):
     def create_app(self):
         # Override create_app method to use for testing
         return create_app()

     def setUp(self):
        # Set up Flask app and client for testing
        self.app = self.create_app()
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

        # Initialize the database
        with self.app.app_context():
            db.create_all()

     def tearDown(self):
        # Clean up after testing
        with self.app.app_context():
            db.session.remove()
            db.drop_all()
        self.app_context.pop()


     def test_signup_post_existing_user(self):
        with self.app.test_request_context('/signup', method='POST', data={
            'Email': 'existing@example.com',
            'First Name': 'John',
            'Last Name': 'Doe',
            'Password': 'password123'
        }):
            response = signup_post()
            self.assertRedirects(response, '/signup')
            self.assert_flashes('Email address already exists', 'error')

     def test_signup_post_new_user(self):
        with self.app.test_request_context('/signup', method='POST', data={
            'Email': 'new@example.com',
            'First Name': 'Jane',
            'Last Name': 'Smith',
            'Password': 'password456'
        }):
            response = signup_post()
            self.assertRedirects(response, '/login')

if __name__ == '__main__':
    unittest.main()