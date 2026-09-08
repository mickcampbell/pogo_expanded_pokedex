import Interface
import PocketMonster


def basic_startup():
    bulbasaur = PocketMonster.Pokemon("Bulbasaur", 1, "Grass", "Poison")
    charmander = PocketMonster.Pokemon("Charmander", 4, "Fire", None, True)
    squirtle = PocketMonster.LimitedEditionPokemon("Squirtle", 7, "Water", event="Summer Event", background="Beach", costume="Sunglasses")
    return [bulbasaur, charmander, squirtle]





def main():
    main_menu = Interface.InitialiseInterface()
    current_menu = main_menu

    global users_pokedex
    users_pokedex = PocketMonster.Pokedex()
    PocketMonster.users_pokedex = users_pokedex
    

    while True:
        current_menu.display_menu()
        choice = current_menu.menu_selection(int(input()))
        if choice is None:
            continue

        next_menu = current_menu.menu_activation(choice)
        if next_menu is None:
            if current_menu is main_menu:
                current_menu.close_interface()
                break
            current_menu = main_menu
        else:
            current_menu = next_menu
        



    

if __name__ == "__main__":
    main()
    