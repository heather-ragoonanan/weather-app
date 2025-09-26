import pytest
from app import app

def test_home_page():
    # Create a test client using our Flask app
    with app.test_client() as client:
        # Make a request to our home page
        response = client.get('/')
        # Check if request was successful
        assert response.status_code == 200
        # Check if our message is in the response
        assert b"Hello! This is my weather app." in response.data

