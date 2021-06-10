import string

from Character import Character
import re
from random import seed
from random import randint
import time

class CharacterPortfolio:
    characters = []
    pattern = re.compile(r"d?([1-9]|[1-9][0-9]|[1-9][0-9][0-9])((\+)([1-9]|[1-9][0-9]|[1-9][0-9][0-9]))?")

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

        if not char:
            return name + " is not a character"
        elif not re.fullmatch(self.pattern,value):
            return "The value of a stat should be a flat number or in the form dX + Y (example d20 + 3)"
        else:
            char.stats[attribute] = value
            return "The attribute has been added"

    def remove_attribute(self,name, attribute):
        char = self.find_by_name(name)

        if not char:
            return name + " is not a character"
        elif char.stats.get(attribute) == None :
            return name + " doesn't have the attribute " + attribute
        else :
            char.stats.pop(attribute)
            return "The attribute " + attribute + " has been removed from the character " + name

    def see_attribute(self,name):
        char = self.find_by_name(name)

        if not char:
            return name + " is not a character"
        elif len(char.stats) == 0 :
            return name + " doesn't have any attribute "
        else :
            str = " The attributes of " + name + " are : \n"
            for key in char.stats :
                str += "[" + key + "] => " + char.stats.get(key) + "\n"
            return str

    def roll_attribute(self,name, attribute):
        char = self.find_by_name(name)

        if not char:
            return name + " is not a character"
        elif char.stats.get(attribute) == None :
            return name + " doesn't have the attribute " + attribute
        else :
            stat_str = char.stats.get(attribute)
            nbr_str = stat_str.strip("d")
            nbr_str = nbr_str.split("+")

            bonus = 0
            if len(nbr_str) > 1 :
                bonus = intify(nbr_str[1].strip(""))

            result = roll(intify(nbr_str[0].strip(" ")), bonus)

            return "```Roll :" +attribute + "= " + stat_str  + "```\nResult = `"+str(result)+"`"




def roll(d: int, plus: int):  # méthode de jet de d avec la possiblilité d'ajouter un entier fixe
    seed(int(round(time.time() * 1000)))  # seed random number generator
    result = randint(1, d)  # generate a random integer
    if (plus != 0):
        result += plus
    return result

def intify(stat: string):  # méthode de traduction d'un string en int
    valeur = int(stat)
    return valeur
