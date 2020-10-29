#! python3

import zombiedice, random

class randomContinue:

    def __init__(self, name):
        self.name = name

    def turn(name, gameState):
        dice_roll_results = zombiedice.roll()

        brains = 0
        while dice_roll_results is not None:
            brains += dice_roll_results['brains']
            if brains >= 1 :
                dice_roll_results = zombiedice.roll() #roll again
            else:
                break