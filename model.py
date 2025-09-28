import requests
from PIL import Image, ImageTk 
from io import BytesIO
# Import needed libraries

class PokemonModel:
    def __init__(self):
        self.number = 1  # start from Bulbasaur
        self.max_pokemon = 151 # Stop when at Mew, could change to include all 1302 pokemon

    def increment(self):
        if self.number < self.max_pokemon:
            self.number += 1
        # Increases while making sure it stays under the max limit

    def decrement(self):
        if self.number > 1:
            self.number -= 1
        # Decreases while ensuring it stays at a min of 1 (could change to go to end when pressing back at 1)

    def get_value(self):
        return self.number
        
    def get_pokemon_data(self):
        # Get the pokemon name and its sprite from poke api
        url = f"https://pokeapi.co/api/v2/pokemon/{self.number}"
        response = requests.get(url)
        data = response.json()
        name = data["name"].title()
        sprite_url = data["sprites"]["front_default"]
        # Get the sprite URL so it can be downloaded to the computer

        # Fetch the sprite image
        img_response = requests.get(sprite_url)
        image_data = img_response.content
        pil_image = Image.open(BytesIO(image_data)).convert("RGBA")
        return name, pil_image
