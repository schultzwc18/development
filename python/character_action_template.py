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

def character_stats(stat_name):
    stats = {
        'level': 1,
        'strength': 8,
        'dexterity': 8,
        'constitution': 8,
        'intelligence': 8,
        'wisdom': 8,
        'charisma': 8

    }

    return stats.get(stat_name, 8)

def character_saving_throws(stat_name):
    saving_throws = {
        'strength': 0,
        'dexterity': 0,
        'constitution': 0,
        'intelligence': 0,
        'wisdom': 0,
        'charisma': 0

    }

    return saving_throws.get(stat_name, 0)

def character_skills(skill_name):
    skills = {
        'athletics': 0,
        'acrobatics': 0,
        'sleight_of_hand': 0,
        'stealth': 0,
        'arcana': 0,
        'history': 0,
        'investigation': 0,
        'nature': 0,
        'religion': 0,
        'animal_handling': 0,
        'insight': 0,
        'medicine': 0,
        'perception': 0,
        'survival': 0,
        'deception': 0,
        'intimidation': 0,
        'performance': 0,
        'persuasion': 0

    }

    return skills.get(skill_name, 0)

def get_stat_modifier(stat_value=10):
    switcher = {
        0: -5,
        1: -5,
        2: -4,
        3: -4,
        4: -3,
        5: -3,
        6: -2,
        7: -2,
        8: -1,
        9: -1,
        10: 0,
        11: 0,
        12: 1,
        13: 1,
        14: 2,
        15: 2,
        16: 3,
        17: 3,
        18: 4,
        19: 4,
        20: 5

    }

    return switcher.get(stat_value, 0)

def get_proficiency_bonus(level=1):
    switcher = {
        1: 2,
        2: 2,
        3: 2,
        4: 2,
        5: 3,
        6: 3,
        7: 3,
        8: 3,
        9: 4,
        10: 4,
        11: 4,
        12: 4,
        13: 5,
        14: 5,
        15: 5,
        16: 5,
        17: 6,
        18: 6,
        19: 6,
        20: 6,

    }

    return switcher.get(level, 2)

def get_skill_stat(skill_name):
    switcher = {
        'athletics': 'strength',
        'acrobatics': 'dexterity',
        'sleight_of_hand': 'dexterity',
        'stealth': 'dexterity',
        'arcana': 'intelligence',
        'history': 'intelligence',
        'investigation': 'intelligence',
        'nature': 'intelligence',
        'religion': 'intelligence',
        'animal_handling': 'wisdom',
        'insight': 'wisdom',
        'medicine': 'wisdom',
        'perception': 'wisdom',
        'survival': 'wisdom',
        'deception': 'charisma',
        'intimidation': 'charisma',
        'performance': 'charisma',
        'persuasion': 'charisma'

    }

    return switcher.get(skill_name, 'strength')

def roll_check(modifier=0, advantage=1):
    first_roll = roll(1, 20)
    second_roll = roll(1, 20)

    if advantage == 0:
        hit = min(first_roll, second_roll)
    elif advantage == 2:
        hit = max(first_roll, second_roll)
    else:
        hit = first_hit

    modified_hit = hit + modifier
    hit_tuple = (hit, modified_hit)
    return hit_tuple

def roll_damage(damage_dice='1d4', modifier=0):
    damage_type = damage_dice.split('d')
    damage_rolls = int(damage_type[0])
    damage_sides = int(damage_type[1])
    damage = roll(damage_rolls, damage_dice)
    modified_damage = damage + modifier
    return modified_damage


def roll_attack(times=1, attack_modifier=0, attack_advantage=1, damage_dice='1d4', damage_modifier=0):
    attacks = []

    for x in range(times):
        current_attack = roll_check(attack_modifier, attack_advantage)
        current_damage = roll_damage(damage_dice, damage_modifier)
        attack_and_damage = "(%d, %d, %d)" %d (current_attack[0], current_attack[1], current_damage)
        attacks.append(attack_and_damage)

    return attacks

if __name__ == "__main__":
    print('test cases here')