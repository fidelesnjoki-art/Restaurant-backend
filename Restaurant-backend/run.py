from app import create_app, db
from app.models import Category, MenuItem
import os

app = create_app()

if __name__ == "__main__":
    app.run(debug=True, port=5000)
