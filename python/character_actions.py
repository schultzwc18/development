from dice_roller import roll

def perform_attack(hit_modifier=0, hit_advantage=False, damage_dice='1d6', damage_modifier=0):
    hit = get_hit(hit_modifier, hit_advantage)
    damage = get_damage(damage_dice, damage_modifier)
    # returning (hit, modified_hit, damage)
    return "(%d, %d, %d)" % (hit[0], hit[1], damage)

def perform_save(modifier=0, advantage=False):
    first_roll = roll(1, 20)
    if advantage:
        second_roll = roll(1, 20)
    else:
        second_roll = -500
    save_roll = max(first_roll, second_roll)
    modified_save = save_roll + modifier
    return "(%d, %d)" % (save_roll, modified_save)

def perform_skill_check(modifier=0, advantage=False):
    first_roll = roll(1, 20)
    if advantage:
        second_roll = roll(1, 20)
    else:
        second_roll = -500
    skill_roll = max(first_roll, second_roll)
    modified_skill = skill_roll + modifier
    return modified_skill


def get_damage(damage_dice='1d4', modifier=0):
    damage_type = damage_dice.split('d')
    dice_rolls = int(damage_type[0])
    dice_sides = int(damage_type[1])
    damage = roll(dice_rolls, dice_sides)
    modified_damage = damage + modifier
    return modified_damage

def get_hit(modifier=0, advantage=False):
    first_roll = roll(1, 20)
    if advantage:
        second_roll = roll(1, 20)
    else:
        second_roll = -500

    hit_roll = max(first_roll, second_roll)
    modified_roll = hit_roll + modifier
    hit_tuple = (hit_roll, modified_roll)
    return hit_tuple

def perform_random_check(sides=20, advantage=False):
    first_roll = roll(1, sides)
    if advantage:
        second_roll = roll(1, sides)
    else:
        second_roll = -500
    return max(first_roll, second_roll)

if __name__ == "__main__":
    print(get_damage('1d10', 2))
    print(get_hit(5, True))
    print(perform_skill_check(10, False))
    print(perform_random_check(10, True))
    print(perform_save(7, True))
    print(perform_attack(4, True, '1d8', 2))