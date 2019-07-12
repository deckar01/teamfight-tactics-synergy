def minimum(count, level):
    return count >= level

def exactly(count, level):
    return count == level

def per_champion(team_size, count, weight):
    return count * weight

def one_champion(team_size, count, weight):
    return weight

def whole_team(team_size, count, weight):
    return team_size * weight

class Synergy:
    match = minimum
    levels = {}

    def __new__(synergy, champion):
        champion.synergies = getattr(champion, 'synergies', [])
        champion.synergies.append(synergy)
        return champion

    @classmethod
    def list(synergy):
        return synergy.__subclasses__()

    @classmethod
    def name(synergy, team_size, count):
        for level, perk in synergy.levels.items():
            if synergy.match(count, level):
                weight, scale = perk
                suffix = 's' if count > 1 else ''
                return '{} {}{}'.format(level, synergy.__name__, suffix)
        return None

    @classmethod
    def score(synergy, team_size, count):
        for level, perk in synergy.levels.items():
            if synergy.match(count, level):
                weight, scale = perk
                return scale(team_size, count, weight)
        return 0

class Class(Synergy):
    def __new__(_class_, champion):
        super().__new__(_class_, champion)
        champion.classes = getattr(champion, 'classes', [])
        champion.classes.append(_class_)
        return champion

class Origin(Synergy):
    def __new__(origin, champion):
        super().__new__(origin, champion)
        champion.origins = getattr(champion, 'origins', [])
        champion.origins.append(origin)
        return champion

class Demon(Origin):
    levels = {
        6: (0.8, per_champion),
        4: (0.6, per_champion),
        2: (0.4, per_champion),
    }


class Dragon(Origin):
    levels = {
        2: (1, per_champion),
    }

class Exile(Origin):
    levels = {
        1: (1, per_champion),
    }

class Glacial(Origin):
    levels = {
        6: (0.45, per_champion),
        4: (0.3, per_champion),
        2: (0.2, per_champion),
    }

class Imperial(Origin):
    levels = {
        4: (1, per_champion),
        2: (1, one_champion),
    }

class Ninja(Origin):
    match = exactly
    levels = {
        4: (0.8, per_champion),
        1: (0.4, per_champion),
    }

class Noble(Origin):
    levels = {
        6: (1.35, whole_team),
        3: (1.35, one_champion),
    }

class Phantom(Origin):
    levels = {
        2: (1, one_champion),
    }

class Pirate(Origin):
    levels = {
        3: (0.2, one_champion),
    }

class Robot(Origin):
    levels = {
        1: (0.1, per_champion),
    }

class Void(Origin):
    levels = {
        3: (0.5, whole_team),
    }

class Wild(Origin):
    levels = {
        4: (0.35, whole_team),
        2: (0.35, per_champion),
    }

class Yordle(Origin):
    levels = {
        6: (0.6, per_champion),
        3: (0.25, per_champion),
    }
    
class Assassin(Class):
    levels = {
        6: (0.35, per_champion),
        3: (0.15, per_champion),
    }

class Blademaster(Class):
    levels = {
        6: (0.9, per_champion),
        3: (0.45, per_champion),
    }

class Brawler(Class):
    levels = {
        4: (0.7, per_champion),
        2: (0.3, per_champion),
    }

class Elementalist(Class):
    levels = {
        3: (1, one_champion),
    }

class Guardian(Class):
    levels = {
        2: (0.4, whole_team),
    }

class Gunslinger(Class):
    levels = {
        4: (1, per_champion),
        2: (0.5, per_champion),
    }

class Knight(Class):
    levels = {
        6: (0.8, per_champion),
        4: (0.4, per_champion),
        2: (0.2, per_champion),
    }

class Ranger(Class):
    levels = {
        4: (0.65, per_champion),
        2: (0.25, per_champion),
    }

class Shapeshifter(Class):
    levels = {
        3: (1, per_champion),
    }

class Sorcerer(Class):
    levels = {
        4: (1, whole_team),
        2: (0.35, whole_team),
    }
