from die_roller import roll

def roll_attack(attacks=1, attack_modifier=0, attack_advantage=False, damage_die='1d6', damage_modifier=0):
    
    attack_rolls = []
    damage_type = damage_die.split('d')
    damage_rolls_number = int(damage_type[0])
    damage_die_sides = int(damage_type[1])
    
    for x in range(attacks):
        # (hit, damage)
        hit = roll_hit(attack_modifier, attack_advantage)
        damage = roll_damage(damage_rolls_number, damage_die_sides, damage_modifier)
        attack_tuple = "(%d, %d)" % (hit, damage)
        attack_rolls.append(attack_tuple)

    return attack_rolls

def roll_save(modifier=0, advantage=False):
    first_hit = roll(1, 20, modifier, 'add')
    if advantage:
        second_hit = roll(1, 20, modifier, 'add')
    else:
        second_hit = -500
    return max(first_hit, second_hit)

def roll_damage(times=1, sides=4, modifier=0):
    dmg = roll(times, sides, modifier, 'add')
    return dmg

def roll_hit(modifier=0, advantage=False):
    first_hit = roll(1, 20, modifier, 'add')
    if advantage:
        second_hit = roll(1, 20, modifier, 'add')
    else:
        second_hit = -500
    return max(first_hit, second_hit)

def roll_skill(modifier=0, advantage=False):
    first_hit = roll(1, 20, modifier, 'add')
    if advantage:
        second_hit = roll(1, 20, modifier, 'add')
    else:
        second_hit = -500
    return max(first_hit, second_hit)

if __name__ == "__main__":
    test_attack = roll_attack(2, 6, False, '2d8', 4)
    print(test_attack)
    test_save = roll_save(2, False)
    print(test_save)
    test_skill = roll_skill(3, False)
    print(test_skill)


