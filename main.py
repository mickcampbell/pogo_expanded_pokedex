import Interface
import PocketMonster




def main():
    users_pokedex = PocketMonster.Pokedex()
    main_menu = Interface.InitialiseInterface(users_pokedex)
    current_menu = main_menu
    

    while True:
        current_menu.display_menu()
        choice = current_menu.menu_selection(int(input()))
        if choice is None:
            continue

        next_menu = current_menu.menu_activation(choice)
        if next_menu is False:
            break
        elif next_menu is None:
            current_menu = main_menu
        else:
            current_menu = next_menu
        




if __name__ == "__main__":
    main()
    