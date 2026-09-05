


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