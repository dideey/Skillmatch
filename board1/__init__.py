from flask import Flask
from flask_sqlalchemy import SQLAlchemy



db = SQLAlchemy()

"""
the function is responsible for creating and configuring an instance
of a flask web application.
"""

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'secret-key-goes-here'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

    db.init_app(app)

    from board1 import pages
    app.register_blueprint(pages.bp)

    

    return app