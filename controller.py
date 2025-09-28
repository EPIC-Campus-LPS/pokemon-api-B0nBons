class PokemonController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        # Initialize variables

        self.view.set_next_callback(self.handle_increment)
        self.view.set_prev_callback(self.handle_decrement)

        # Initialize display with Bulbasaur (first pokemon)
        self.update_view()

    def handle_increment(self):
        self.model.increment()
        self.update_view() # Update the view as soon as user clicks next

    def handle_decrement(self):
        self.model.decrement()
        self.update_view() # Just like the other one, updates the view when user clicks previous

    def update_view(self):
        # Get data from model
        name, image = self.model.get_pokemon_data()
        # Update view
        self.view.set_label(f"{self.model.get_value()}: {name}") #Print pokemon number, and the pokemon name
        self.view.set_image(image) # Set pokemon sprite
