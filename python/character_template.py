"""

    document skills and skill proficiencies
    document saving throws and proficiencies
    document stats

"""

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

if __name__ == "__main__":
    print(get_stat_modifier(13))
    print(get_proficiency_bonus(5))
    print(get_skill_stat('insight'))