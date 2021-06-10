from CharacterPortfolio import CharacterPortfolio


class MessageHandler:
    def __init__(self):
        pass

    APP_FLAG = "!dm"

    HELP_FLAG = "help"

    HELP_MESSAGE = "Type **!dm help** to get the list of command"

    NOT_RECOGNIZED_MESSAGE = "Commande non reconnu"

    CHARACTER_FLAG = "character"
    CHARACTER_FLAG2 = "char"
    CHARACTER_FLAG3 = "perso"

    ATTRIBUTE_FLAG1 = "attribute"
    ATTRIBUTE_FLAG2 = "attr"

    ROLL_FLAG = "roll"

    ADD_FLAG = "add"
    CREATE_FLAG = "create"
    DELETE_FLAG = "delete"

    chars = CharacterPortfolio()


    def handle_message(self, message):
        cut_message = message.split(" ")

        if cut_message[0] != self.APP_FLAG:
            return False

        if len(cut_message) < 2:
            return self.HELP_MESSAGE

        if cut_message[1] == self.HELP_FLAG:
            return """*COMMANDS*
            
Create a character : **!dm char create [Character name]**
Delete a character : **!dm char delete [Character name]**
            
Add or modify an attribute of a character : **!dm attr add [Character name] [Attr name] [Attr value]**
Attribute values are either numbers(Like 6) 
Or expression of a dice roll (ex **d20** for the roll of a d20
or d10+3 for the roll of a d10 with a +3 bonus) 
        
Delete an attribute of a character : **!dm attr delete [Character name] [Attr name]**
"""

        if cut_message[1] == self.CHARACTER_FLAG or cut_message[1] == self.CHARACTER_FLAG2 or cut_message[1] == self.CHARACTER_FLAG3:
            if len(cut_message) < 3:
                return self.HELP_MESSAGE
            elif cut_message[2] == self.CREATE_FLAG:
                if len(cut_message) < 4:
                    return "You need to add the name of your character after **!dm character create**"
                else:
                    return self.chars.add_character(cut_message[3])
            elif cut_message[2] == self.DELETE_FLAG:
                if len(cut_message) < 4:
                    return "You need to add the name of the character after **!dm character create**"
                else:
                    return self.chars.remove_character(cut_message[3])
            else:
                return self.NOT_RECOGNIZED_MESSAGE

        elif cut_message[1] == self.ATTRIBUTE_FLAG1 or self.ATTRIBUTE_FLAG2:
            if len(cut_message) < 3:
                return self.HELP_MESSAGE
            elif cut_message[2] == self.ADD_FLAG:
                if len(cut_message) < 4:
                    return "You need to add the name of your character after **!dm attribute add**"
                else:
                    if len(cut_message) < 5:
                        return "You need to add the name of the attribute after the name of the character"
                    else:
                        # TODO: Add method
                        pass
            elif cut_message[2] == self.DELETE_FLAG:
                if len(cut_message) < 4:
                    return "You need to add the name of the character and the " \
                           "name of the attribute after **!dm attribute delete**"
                else:
                    if len(cut_message) < 5:
                        return "You need to add the name of the attribute after the name of the character"
                    else:
                        # TODO: Add method
                        pass
            elif cut_message[1] == self.ROLL_FLAG :
                if len(cut_message) < 3:
                    return self.HELP_MESSAGE
                if len(cut_message) < 4:
                    return "You need to add the name of the stat after **!dm roll [character]**"
                else:
                    # TODO: Add method
                        pass
            else:
                return self.NOT_RECOGNIZED_MESSAGE
