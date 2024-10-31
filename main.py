from fastapi import FastAPI, HTTPException, status
from starlette import status

from models.db import db
from models.models import Sheep
app = FastAPI()

@app.get("/sheep/{id}", response_model=Sheep)
def read_sheep(id: int):
    # Check if the sheep ID exists
    if (id not in db.data):
        raise HTTPException(status_code = 404, detail="Sheep not found")

    return db.get_sheep(id)

@app.post("/sheep/", response_model=Sheep, status_code = status.HTTP_201_CREATED)
def add_sheep(sheep: Sheep):
    # Check if the sheep ID already exists to avoid duplicates
    if sheep.id in db.data:
        raise HTTPException(status_code = 400, detail="Sheep with this ID already exists")

    # Add the new sheep to the database
    db.data[sheep.id] = sheep
    return sheep    #return the newly added sheep attributes

# Extra Credit Starts Here ------------------------------------------------------------------------------------------------------------------------------
@app.delete("/sheep/{id}", status_code = status.HTTP_204_NO_CONTENT)
def remove_sheep(id: int):
    # Check if the sheep ID exists
    if (id not in db.data):
        raise HTTPException(status_code = 404, detail="Sheep not found")

    # Remove Sheep From DB

    deleted_sheep = db.data[id]
    db.delete_sheep(id)
    return deleted_sheep

@app.put("/sheep/{id}", response_model=Sheep)
def update_sheep(id: int, sheep: Sheep):

    # Check if the sheep ID exists
    if (id not in db.data):
        raise HTTPException(status_code=404, detail="Sheep not found")

    # Update the sheep in the database
    db.update_sheep(id, sheep)
    return sheep

@app.get("/sheep/", response_model=Sheep)
def read_all_sheep(self):

    # Return all the sheep currently in the DB
    return db.read_all_sheep()

#Extra Credit Ends Here --------------------------------------------------------------------------------------------------------------------------------
