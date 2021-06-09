import Character

class CharacterPortfolio:
    characters = []

    def add_character(self, name):
        new_char = Character(name)
        self.characters.append(new_char)


    def find_by_name(self, name):
        for character in self.characters:
            if character.name == name:
                return character
        return False

    def remove_character(self, name):
        self.characters.remove(self.find_by_name(name))

    def modif_character(self, name):
        pass                                                                                                                                                                                          d        f




