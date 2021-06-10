from Character import Character
import re


class CharacterPortfolio:
    characters = []
    pattern = re.compile(r"d([1-9]|[1-9][0-9]|[1-9][0-9][0-9])((\+)([1-9]|[1-9][0-9]|[1-9][0-9][0-9]))?")

    def add_character(self, name):
        new_char = Character(name)
        if not self.find_by_name(name):
            self.characters.append(new_char)
            return name + " has been added"
        else:
            return name + " is already in the list"

    def find_by_name(self, name):
        for character in self.characters:
            if character.name == name:
                return character
        return False

    def remove_character(self, name):
        if not self.find_by_name(name) :
            self.characters.remove(self.find_by_name(name))
            return name + " has been deleted"
        else:
            return name + " does not exist"

    def add_attribute(self,name, attribute, value):
        char = self.find_by_name(name)

        if not self.find_by_name(name):
            return name + " is not a character"
        elif re.fullmatch(self.pattern,value):
            return "The value of a stat should be a flat number or in the form dX + Y (example d20 + 3)"
        else:
            char.stats[attribute] = value
            return "The attribute has been added"



