import sys
sys.path.insert(0, '/home/dideey123/skillmatch')

from board1 import create_app
from board1.models import db

# Create the Flask app
app = create_app()

# Access the SQLAlchemy database object
with app.app_context():
    # Create the necessary database tables based on your model definitions
    db.create_all()

print("Database created successfully.")