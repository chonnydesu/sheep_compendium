from models.models import Sheep
from typing import Dict

class FakeDB:
    def __init__(self):
        self.data: Dict[int,Sheep] = {}

    def get_sheep(self,id: int) -> Sheep:
        return self.data.get(id)

    def add_sheep(self,sheep: Sheep):
        # Check if the sheep ID already exists
        if sheep.id in self.data:
            raise ValueError("Sheep with this ID already exists")

        # Add the new sheep to the database
        self.data[sheep.id] = sheep
        return sheep  # Return the created sheep

    # Extra Credit Starts Here ------------------------------------------------------------------------------------------------------------------------------

    def delete_sheep(self,id: int):
        # Check if the sheep ID exists
        if id not in self.data:
            raise ValueError("Sheep not found")

        # Delete the sheep from the database
        deleted_sheep = self.data[id]
        del self.data[id]
        return deleted_sheep

    def update_sheep(self,id: int, sheep:Sheep):
        # Check if the sheep ID exists
        if id not in self.data:
            raise ValueError("Sheep not found")

        if (self.data[sheep.id] == sheep):
            raise ValueError("Sheep already in database!")

        # REPLACE the new sheep into to the database @ID
        self.data[sheep.id] = sheep
        return sheep  # Return the newly replaced sheep

    def read_all_sheep(self):
        return self.data.values()

    # Extra Credit Ends Here --------------------------------------------------------------------------------------------------------------------------------


db = FakeDB()
db.data = {
    1: Sheep(id="1",name="Spice",breed="Gotland",sex="ewe"),
    2: Sheep(id="2",name="Blondie",breed="Polypay",sex="ram"),
    3: Sheep(id="3",name="Deedee",breed="Jacobs Four Horns",sex="ram"),
    4: Sheep(id="4",name="Rommy",breed="Romney",sex="ewe"),
    5: Sheep(id="5",name="Vala",breed="Valais Blacknose",sex="ewe"),
    6: Sheep(id="6",name="Esther",breed="Border Leicester",sex="ewe")
}