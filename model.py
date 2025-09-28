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

    def decrement(self):
        if self.number > 1:
            self.number -= 1

    def get_value(self):
        return self.number

    def get_pokemon_data(self):
        # Get the pokemon name and its sprite from poke api
        url = f"https://pokeapi.co/api/v2/pokemon/{self.number}"
        response = requests.get(url)
        data = response.json()
        name = data["name"].title()
        sprite_url = data["sprites"]["front_default"]

        # Fetch the sprite image
        img_response = requests.get(sprite_url)
        image_data = img_response.content
        pil_image = Image.open(BytesIO(image_data)).convert("RGBA")
        return name, pil_image
