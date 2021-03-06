import random

def roll_dice(sides=20, modifier=0):
    dice_roll = random.randint(1, sides) + modifier
    return dice_roll

def get_roll_total(rolls = [1]):
    roll_total = sum(rolls)
    return roll_total

def roll(times=1, sides=20, modifier=0):
    rolls = []

    for x in range(times):
        current_roll = roll_dice(sides, modifier)
        rolls.append(current_roll)

    total = get_roll_total(rolls)
    return total
    
if __name__ == "__main__":
    roll(2, 10, 7)