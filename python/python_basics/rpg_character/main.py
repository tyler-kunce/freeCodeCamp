full_dot = '●'
empty_dot = '○'

def create_character(name, strength, intelligence, charisma):

    # CONDITIONAL CHECKS AGAINST NAME FORMAT
    if not isinstance(name, str):
        return 'The character name should be a string'
    if name == '':
        return 'The character should have a name'
    if len(name) > 10:
        return 'The character name is too long'
    if ' ' in name:
        return 'The character name should not contain spaces'
    
    # CONDITIONAL CHECKS AGAINST STATS FORMAT
    if not isinstance(strength, int):
        return 'All stats should be integers'
    if not isinstance(intelligence, int):
        return 'All stats should be integers'
    if not isinstance(charisma, int):
        return 'All stats should be integers'
    if strength < 1:
        return 'All stats should be no less than 1'
    if intelligence < 1:
        return 'All stats should be no less than 1'
    if charisma < 1:
        return 'All stats should be no less than 1'
    if strength > 4:
        return 'All stats should be no more than 4'
    if intelligence > 4:
        return 'All stats should be no more than 4'
    if charisma > 4:
        return 'All stats should be no more than 4'
    if (strength + intelligence + charisma) != 7:
        return 'The character should start with 7 points'
    
    # CONDITIONALS PASSED, RETURN CHARACTER NAME & STATS
    full_stat_str = strength * full_dot
    empty_stat_str = (10 - strength) * empty_dot
    stat_str = full_stat_str+ empty_stat_str
    full_stat_intel = intelligence * full_dot
    empty_stat_intel = (10 - intelligence) * empty_dot
    stat_intel = full_stat_intel + empty_stat_intel
    full_stat_char = charisma * full_dot
    empty_stat_char = (10 - charisma) * empty_dot
    stat_char = full_stat_char + empty_stat_char
    return f'{name}\nSTR {stat_str} \nINT {stat_intel} \nCHA {stat_char}'