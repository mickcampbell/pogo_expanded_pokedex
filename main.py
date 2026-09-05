

from PocketMonster import Pokemon, LimitedEditionPokemon


def basic_startup():
    bulbasaur = Pokemon("Bulbasaur", 1, "Grass", "Poison")
    charmander = Pokemon("Charmander", 4, "Fire", None, True)
    squirtle = LimitedEditionPokemon("Squirtle", 7, "Water", event="Summer Event", background="Beach", costume="Sunglasses")
    return [bulbasaur, charmander, squirtle]





def main():
    print("Welcome to your Pokédex for Pokémon Go!")
    starters = basic_startup()
    for starter in starters:
        print(f"{starter.name} (#{starter.pokedex_number}) - Type: {starter.type1}" + (f"/{starter.type2}" if starter.type2 else ""))
        if starter.shiny:
            print("This Pokémon is shiny!")
        if isinstance(starter, LimitedEditionPokemon):
            if starter.event:
                print(f"Event: {starter.event}")
            if starter.background:
                print(f"Background: {starter.background}")
            if starter.costume:
                print(f"Costume: {starter.costume}")


if __name__ == "__main__":
    main()
    