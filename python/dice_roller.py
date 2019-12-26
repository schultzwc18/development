import random

def get_roll(sides=20):
    roll = random.randint(1, sides)
    return roll


def get_roll_total(rolls = [1]):
    roll_total = sum(rolls)
    return roll_total


def roll(times=1, sides=20):
    rolls = []
    for x in range(times):
        current_roll = get_roll(sides)
        rolls.append(current_roll)

    total_roll = get_roll_total(rolls)
    return total_roll

if __name__ == "__main__":
    print(get_roll(20))
    print(get_roll_total([5, 10, 15]))
    print(roll(2, 4))