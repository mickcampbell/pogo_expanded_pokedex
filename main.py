import Interface
from PocketMonster import Pokemon, LimitedEditionPokemon


def basic_startup():
    bulbasaur = Pokemon("Bulbasaur", 1, "Grass", "Poison")
    charmander = Pokemon("Charmander", 4, "Fire", None, True)
    squirtle = LimitedEditionPokemon("Squirtle", 7, "Water", event="Summer Event", background="Beach", costume="Sunglasses")
    return [bulbasaur, charmander, squirtle]





def main():
    interface = Interface.Interface()
    pokemon_list = basic_startup()

    for pokemon in pokemon_list:
        interface.add_pokemon(pokemon)
    interface.display_pokemon()

if __name__ == "__main__":
    main()
    