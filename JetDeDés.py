import string
from random import seed
from random import randint

def d(d: int, plus: int): # méthode de jet de d avec la possiblilité d'ajouter un entier fixe
    # Pensez à supprimer les prints de debug
    print('On lance un d'+d+' et on ajoute '+plus)
    seed(1) # seed random number generator
    result = randint(1,d) # generate a random integer
    if (plus != 0):
        result += plus
    print('On obtient : '+result)
    return result



def roll(stat: string): # méthode de traduction d'un string en int
    valeur = int(stat)
    return valeur