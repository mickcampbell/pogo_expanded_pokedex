
users_pokedex = None

class Pokemon:
    def __init__(self, name, pokedex_number, type1, type2=None, shiny=False):
        self.name = name
        self.pokedex_number = pokedex_number
        self.type1 = type1
        self.type2 = type2
        self.shiny = shiny


class LimitedEditionPokemon(Pokemon):
    def __init__(self, name, pokedex_number, type1, type2=None, shiny=False, event=None, 
                 background=None, costume=None):
        super().__init__(name, pokedex_number, type1, type2, shiny)
        self.event = event
        self.background = background
        self.costume = costume

class Pokedex:
    def __init__(self):
        self.pokemon_list = []

    def add_pokemon(self, pokemon):
        self.pokemon_list.append(pokemon)

    def display_pokedex(self):
        for pokemon in self.pokemon_list:
            print(f"{pokemon.name} (#{pokemon.pokedex_number}) - Type: {pokemon.type1}" + (f"/{pokemon.type2}" if pokemon.type2 else ""))
            if pokemon.shiny:
                print("This Pokémon is shiny!")
            if isinstance(pokemon, LimitedEditionPokemon):
                if pokemon.event:
                    print(f"Event: {pokemon.event}")
                if pokemon.background:
                    print(f"Background: {pokemon.background}")
                if pokemon.costume:
                    print(f"Costume: {pokemon.costume}")