import time
import random

dice1 = """
__________
|         |
|         |
|    O	  |
|         |
|_________|"""

dice2 = """
__________
|         |
|      O  |
|    	  |
|  O      |
|_________|"""

dice3 = """
__________
|         |
|      O  |
|    O	  |
|  O      |
|_________|"""

dice4 = """
__________
|         |
|  O   O  |
|    	  |
|  O   O  |
|_________|"""

dice5 = """
__________
|         |
|  O   O  |
|    O	  |
|  O   O  |
|_________|"""

dice6 = """
__________
|         |
|  O   O  |
|  O   O  |
|  O   O  |
|_________|"""

dice_list = (dice1, dice2, dice3, dice4, dice5, dice6)

# Seconds that the dice animation will be shown
animation_duration_time = 10
time_end = time.time() + animation_duration_time


def roll_dice():
    while time.time() < time_end:
        print(random.choice(dice))


time.sleep(1)

def dice():
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        dice = die1 + die2
        print("You roll a", die1, "and", die2, "for a total of", dice)
        print(dice_list[die1 - 1])
        print(dice_list[die2 - 1], '\n')

        return dice