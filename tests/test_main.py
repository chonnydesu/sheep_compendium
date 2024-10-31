# Import TestClient to simulate API requests
from fastapi.testclient import TestClient

# Import the FastAPI app instance from the controller module
from main import app
from models.models import Sheep

# Create a TestClient instance for the FastAPI app
client = TestClient(app)

# Define a test function for reading a specific sheep
def test_read_sheep():
    # Send a GET request to the endpoint "/sheep/1"
    response = client.get("/sheep/1")

    # Assert that the response status code is 200 (OK)
    assert response.status_code == 200

    # Assert that the response JSON matches the expected data
    assert response.json() == {
        # Expected JSON Structure
        "id" : 1,
        "name" : "Spice",
        "breed" : "Gotland",
        "sex" : "ewe"
    }

def test_add_sheep():

    # test sheep
    newSheep = {"id" : 7,
                "name" : "Ellie",
                "breed" : "F1",
                "sex" : "ewe"
                }

    response = client.post("/sheep/", json=newSheep)

    assert response.status_code == 201

    assert response.json() == {
        # Expected JSON Structure
        "id": 7,
        "name": "Ellie",
        "breed": "F1",
        "sex": "ewe"
    }

    responseTwo = client.get("/sheep/7")
    assert responseTwo.status_code == 200

# Extra Credit Starts Here ------------------------------------------------------------------------------------------------------------------------------
def test_remove_sheep():
    # Add a test sheep
    new_sheep = {
        "id": 8,
        "name": "Spice",
        "breed": "Gotland",
        "sex": "ewe"
    }
    response_post = client.post("/sheep/", json=new_sheep)
    assert response_post.status_code == 201  # Ensure sheep was created

    # Now delete the sheep
    response_delete = client.delete("/sheep/8")
    assert response_delete.status_code == 204  # expect (successfully deleted)

    # Verify the sheep was deleted
    response_get = client.get("/sheep/8")
    assert response_get.status_code == 404  # Should return 404, sheep not found

def test_update_sheep():
    # Add a test sheep
    new_sheep = {
        "id": 4,
        "name": "Jasper",
        "breed": "Beagle",
        "sex": "male"
    }

    # Pull aside the original sheep
    original_sheep = client.get("/sheep/4").json()

    # Replace the sheep
    response_replace = client.put("/sheep/4", json=new_sheep)
    assert response_replace.status_code == 200  # expect (OK)
    assert client.get("/sheep/4").json() != original_sheep
    assert client.get("/sheep/4").json() == new_sheep

def test_read_all_sheep():
    # Read all sheep from the DB
    all_sheep = list(client.get("/sheep").json())

    # Assert that the number of sheep is as expected (6)
    assert len(all_sheep), 6

# Extra Credit Ends Here --------------------------------------------------------------------------------------------------------------------------------
