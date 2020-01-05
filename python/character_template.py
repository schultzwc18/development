import character_actions

"""

    This file is not meant to be populated and saved. 
    Create a copy of this file for each character that's being created

"""

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

def get_stat_bonus(stat_name='strength'):
    stat_value = character_stats(stat_name)
    stat_bonus = character_actions.get_stat_modifier(stat_value)
    return stat_bonus

def get_saving_throw_bonus(stat_name):
    stat_bonus = get_stat_bonus(stat_name)
    level = character_stats('level')
    proficiency_bonus = character_actions.get_proficiency_bonus(level)
    saving_throw_proficiency = character_saving_throws(stat_name)
    saving_throw_bonus = stat_bonus + (saving_throw_proficiency * proficiency_bonus)
    return saving_throw_bonus

def get_skill_bonus(skill_name='athletics'):
    skill_stat = character_actions.get_skill_stat(skill_name)
    skill_bonus = get_stat_bonus(skill_stat)
    return skill_bonus

def strength_saving_throw(advantage=1):
    stat = 'strength'
    saving_throw_bonus = get_saving_throw_bonus(stat)
    saving_throw_roll = character_actions.roll_check(saving_throw_bonus, advantage)
    return saving_throw_roll

def dexterity_saving_throw(advantage=1):
    stat = 'dexterity'
    saving_throw_bonus = get_saving_throw_bonus(stat)
    saving_throw_roll = character_actions.roll_check(saving_throw_bonus, advantage)
    return saving_throw_roll

def constitution_saving_throw(advantage=1):
    stat = 'constitution'
    saving_throw_bonus = get_saving_throw_bonus(stat)
    saving_throw_roll = character_actions.roll_check(saving_throw_bonus, advantage)
    return saving_throw_roll

def intelligence_saving_throw(advantage=1):
    stat = 'intelligence'
    saving_throw_bonus = get_saving_throw_bonus(stat)
    saving_throw_roll = character_actions.roll_check(saving_throw_bonus, advantage)
    return saving_throw_roll

def wisdom_saving_throw(advantage=1):
    stat = 'wisdom'
    saving_throw_bonus = get_saving_throw_bonus(stat)
    saving_throw_roll = character_actions.roll_check(saving_throw_bonus, advantage)
    return saving_throw_roll

def charisma_saving_throw(advantage=1):
    stat = 'charisma'
    saving_throw_bonus = get_saving_throw_bonus(stat)
    saving_throw_roll = character_actions.roll_check(saving_throw_bonus, advantage)
    return saving_throw_roll


def physical_attack(attack_stat='strength', proficient=1, attack_advantage=1, damage_dice='1d4', damage_bonus=True):
    character_level = character_stats('level')
    stat_bonus = get_stat_bonus(attack_stat)
    proficiency_bonus = character_actions.get_proficiency_bonus(character_level)
    attack_modifier = stat_bonus + (proficient * proficiency_bonus)
    
    if damage_bonus:
        damage_modifier = stat_bonus
    else:
        damage_modifier = 0

    attack = character_actions.roll_attack(1, attack_modifier, attack_advantage, damage_dice, damage_modifier)
    return attack

def main_hand_attack(damage_dice='1d4'):
    main_hand = physical_attack('strength', 1, 1, damage_dice, True)
    return main_hand

def off_hand_attack(damage_dice='1d4'):
    off_hand = physical_attack('strength', 1, 1, damage_dice, False)
    return off_hand

if __name__ == "__main__":
    print(physical_attack('dexterity', 0, 2, '1d6'))
    print(main_hand_attack('1d8'))
    print(off_hand_attack('1d6'))
    print(dexterity_saving_throw())