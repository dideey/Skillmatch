from flask import Flask

from board1 import pages

"""
the function is responsible for creating and configuring an instance
of a flask web application.
"""

def create_app():
    app = Flask(__name__)
    app.register_blueprint(pages.bp)

    return app