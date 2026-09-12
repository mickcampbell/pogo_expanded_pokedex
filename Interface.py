
import PocketMonster




class Interface():
    def __init__(self, pokedex):
        self.title = "Interface Placeholder"
        self.description = "This is a placeholder for the interface. It will be replaced with a proper GUI in the future."
        self.menu_items = [("Option 1", self.you_shouldnt_be_seeing_this), ("Option 2", self.you_shouldnt_be_seeing_this), ("Option 3", self.you_shouldnt_be_seeing_this)]
        self.pokedex = pokedex

    def display_menu(self):
        print(f"{self.title}\n{self.description}")
        for index, item in enumerate(self.menu_items, start=1):
            print(f"{index}. {item[0]}")
        print("Please select an option by entering the corresponding number.")

    def menu_selection(self, selection):
        if selection < 1 or selection > len(self.menu_items):
            print("Invalid selection. Please try again.")
            return None
        return selection


    def menu_activation(self, selection):
        action = self.menu_items[selection - 1][1]
        if isinstance(action, type) and issubclass(action, Interface):
            return action(self.pokedex)
        if callable(action):
            return action()
        return action

    def you_shouldnt_be_seeing_this(self):
        print("You shouldn't be seeing this. This is a placeholder for the interface. It will be replaced with a proper GUI in the future.")

    def close_interface(self):
        print("Closing the interface. Thank you for using the Pokémon Interface!")
        return False



class MainMenuInterface(Interface):
    def __init__(self, pokedex):
        super().__init__(pokedex)
        self.title = "Main Menu"
        self.description = "Welcome to the Pokémon Interface! Would you like to see all your Pokémon or add a new one?"
        self.menu_items = [("View Pokémon", PokedexInterface), ("Add a new Pokémon", AddPokemonInterface), ("Exit", self.close_interface)]


class InitialiseInterface(Interface):
    def __init__(self, pokedex):
        super().__init__(pokedex)
        self.title = "Start Up Interface"
        self.description = "Starting up the Pokedex. Would you like a system generated Pokédex or would you like to add your own Pokémon?"
        self.menu_items = [("System Generated Pokédex", SystemAddPokemonInterface), ("Add Your Own Pokémon", MainMenuInterface), ("Exit", self.close_interface)]




class PokedexInterface(Interface):
    def __init__(self, pokedex):
        super().__init__(pokedex)
        self.title = "Pokedex Interface"
        self.description = "This interface displays a list of Pokémon and their details."
        self.pokedex = pokedex
        
        if self.pokedex is None:
            raise RuntimeError("The shared Pokedex has not been initialized.")
        self.menu_items = [("Display all Pokémon", self.display_pokemon), ("Back to Main Menu", None)]

    def display_pokemon(self):
        if not self.pokedex.pokemon_list:
            print("Your Pokedex is empty. Please add some Pokémon first.")
            return
        self.pokedex.display_pokedex()

    def menu_activation(self, selection):
        if selection == 1:
            self.display_pokemon()
            return self
        elif selection == 2:
            return MainMenuInterface(self.pokedex)
        return None


    




class AddPokemonInterface(Interface):
    def __init__(self, pokedex):
        super().__init__(pokedex)
        self.title = "Add Pokémon Interface"
        self.description = "This interface allows you to add a new Pokémon to the Pokedex."
        self.menu_items = [("Add Regular Pokémon", self.add_regular_pokemon), ("Add Limited Edition Pokémon", self.add_limited_edition_pokemon), ("Back to Main Menu", None)]

    def add_regular_pokemon(self, name, pokedex_number, type1, type2=None, shiny=False):
        new_pokemon = PocketMonster.Pokemon(name, pokedex_number, type1, type2, shiny)
        return new_pokemon

    def add_limited_edition_pokemon(self, name, pokedex_number, type1, event=None, background=None, costume=None):
        new_pokemon = PocketMonster.LimitedEditionPokemon(name, pokedex_number, type1, None, False, event=event, background=background, costume=costume)
        return new_pokemon

    def menu_activation(self, selection):
        if selection == 1:
            name = input("Enter Pokémon name: ")
            pokedex_number = int(input("Enter Pokédex number: "))
            type1 = input("Enter primary type: ")
            type2 = input("Enter secondary type (or leave blank): ") or None
            shiny_input = input("Is it shiny? (yes/no): ").strip().lower()
            shiny = shiny_input == "yes"
            new_pokemon = self.add_regular_pokemon(name, pokedex_number, type1, type2, shiny)
            self.pokedex.add_pokemon(new_pokemon)
            print(f"{name} has been added to your Pokedex.")
            return self
        elif selection == 2:
            name = input("Enter Pokémon name: ")
            pokedex_number = int(input("Enter Pokédex number: "))
            type1 = input("Enter primary type: ")
            event = input("Enter event (or leave blank): ") or None
            background = input("Enter background (or leave blank): ") or None
            costume = input("Enter costume (or leave blank): ") or None
            new_pokemon = self.add_limited_edition_pokemon(name, pokedex_number, type1, event, background, costume)
            self.pokedex.add_pokemon(new_pokemon)
            print(f"{name} has been added to your Pokedex.")
            return self
        elif selection == 3:
            return MainMenuInterface(self.pokedex)
        return None


class SystemAddPokemonInterface(Interface):
    def __init__(self, pokedex):
        super().__init__(pokedex)

    def system_add_pokemon(self, pokemon, pokedex_interface):
        pokedex_interface.pokedex.add_pokemon(pokemon)

    def display_menu(self):
        print("Adding system-generated Pokémon to your Pokedex. Press 1 to continue.")

    def menu_selection(self, selection):
        return 1

    def menu_activation(self, selection):
        if selection == 1:
            for pokemon in self.basic_startup():
                self.pokedex.add_pokemon(pokemon)
            return MainMenuInterface(self.pokedex)
        return None

    def basic_startup(self):
        bulbasaur = PocketMonster.Pokemon("Bulbasaur", 1, "Grass", "Poison")
        charmander = PocketMonster.Pokemon("Charmander", 4, "Fire", None, True)
        squirtle = PocketMonster.LimitedEditionPokemon("Squirtle", 7, "Water", event="Summer Event", background="Beach", costume="Sunglasses")
        return [bulbasaur, charmander, squirtle]
