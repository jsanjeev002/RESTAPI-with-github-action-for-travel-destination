from main import app
import json

def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert response.json == {"message": "Welcome to the Travel API!"}

def test_add_destination():
    client = app.test_client()
    response = client.post("/destinations", json={
        "destination": "Paris",
        "country": "France",
        "rating": 4.8
    })
    assert response.status_code == 201
    assert response.json["destination"] == "Paris"

def test_get_destinations():
    client = app.test_client()
    response = client.get("/destinations")
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_get_invalid_destination():
    client = app.test_client()
    response = client.get("/destinations/9999")  # Assuming it doesn't exist
    assert response.status_code == 404
