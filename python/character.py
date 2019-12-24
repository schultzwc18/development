import actions

"""

provide character stats (strength, constitution, dexterity, etc.) then it can calculate the appropriate modifier <- dictionary
pass level to get appropriate proficiency
dictionary of skills and whether proficient
lists of each skill and their related stat
list of each saving throw and whether they're proficient


"""

def get_proficiency(level=1):
    proficiency_bonus = {1: 2, 2: 2, 3: 2, 4: 2, 5: 3, 6: 3, 7: 3, 8: 3, 9: 4, 10: 4, 11: 4, 12: 4, 13: 5, 14: 5, 15: 5, 16: 5, 17: 6, 18: 6, 19: 6, 20: 6}
    return proficiency_bonus.get(level)

def get_skill_modifier(level, skill):
    strength_skills = ['athletics']
    dexterity_skills = ['acrobatics', 'sleight_of_hand', 'stealth']
    intelligence_skills = ['arcana', 'history', 'investigation', 'nature', 'religion']
    wisdom_skills = ['animal_handling', 'insight', 'medicine', 'perception', 'survival']
    charisma_skills = ['deception', 'intimidation', 'performance', 'persuasion']


if __name__ == "__main__":
    print(get_proficiency(2))
    print(get_proficiency(5))
    print(get_proficiency(19))