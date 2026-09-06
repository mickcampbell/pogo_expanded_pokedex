
from PocketMonster import Pokemon, LimitedEditionPokemon


class Interface():
    def __init__(self):
        self.pokemon_list = []

    def add_pokemon(self, pokemon):
        self.pokemon_list.append(pokemon)

    def display_pokemon(self):
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