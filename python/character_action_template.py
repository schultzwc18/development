import character_actions

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



def roll_saving_throw(stat_name='strength', advantage=False):
    stat_value = character_stats(stat_name)
    saving_throw_proficiency = character_saving_throws(stat_name)
    level = character_stats('level')
    level_proficiency = character_template.get_proficiency_bonus(level)
    stat_modifier = character_template.get_stat_modifier(stat_value)

    saving_throw_modifier = stat_modifier + int(level_proficiency * saving_throw_proficiency)
    save_roll = character_actions.perform_save(saving_throw_modifier, advantage)
    print(save_roll)

def roll_skill_check(skill_name='athletics', advantage=False):
    skill_stat = character_template.get_skill_stat(skill_name)
    stat_value = character_stats(skill_stat)
    stat_modifier = character_template.get_stat_modifier(stat_value)
    skill_proficiency = character_skills(skill_name)
    level = character_stats('level')
    level_proficiency = character_template.get_proficiency_bonus(level)

    skill_check_modifier = stat_modifier + int(level_proficiency * skill_proficiency)
    skill_roll = character_actions.perform_skill_check(skill_check_modifier, advantage)
    print(skill_roll)

def roll_damage(damage_stat='strength', damage_dice='1d4', additional_modifiers=0):
    stat_value = character_stats(damage_stat)

    if damage_stat == 'magic':
        stat_modifier = 0
    else:
        stat_modifier = character_template.get_stat_modifier(stat_value)

    damage_modifier = stat_modifier + additional_modifiers

    damage = character_actions.get_damage(damage_dice, damage_modifier)
    half_damage = damage // 2
    print("(%d, %d)" % (damage, half_damage))


def roll_attack(times=1, hit_stat='strength', damage_dice='1d4', additional_damage_modifiers=0, hit_advantage=False):
    stat_value = character_stats(hit_stat)
    stat_modifier = character_template.get_stat_modifier(stat_value)
    level = character_stats('level')
    level_proficiency = character_template.get_proficiency_bonus(level)

    hit_modifier = stat_modifier + level_proficiency
    damage_modifier = stat_modifier + additional_damage_modifiers

    for x in range(times):
        hit_roll = character_actions.perform_attack(hit_modifier, hit_advantage, damage_dice, damage_modifier)
        print(hit_roll)

def roll_spell(hit_stat='wisdom', damage_dice='1d4', additional_damage_modifiers=0):
    print('hello world')


if __name__ == "__main__":
    roll_attack(1, 'strength', '1d8', 0, False)