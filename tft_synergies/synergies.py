def total_weight(champions):
    return sum(champion.weight for champion in champions)

def average_weight(champions):
    return total_weight(champions) / len(champions)

def minimum(group, level):
    return len(group) >= level

def exactly(group, level):
    return len(group) == level

def static_effect(team, group, weight):
    return weight

def per_member(team, group, weight):
    return weight * total_weight(group)

def per_teammate(team, count, weight):
    return weight * total_weight(team.champions)

def random_member(team, group, weight):
    return weight * average_weight(group)

def random_teammate(team, group, weight):
    return weight * average_weight(team.champions)

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
    def name(synergy, team, group):
        for level, perk in synergy.levels.items():
            if synergy.match(group, level):
                weight, scale = perk
                suffix = 's' if len(group) > 1 else ''
                return '{} {}{}'.format(level, synergy.__name__, suffix)
        return None

    @classmethod
    def score(synergy, team, group):
        for level, perk in synergy.levels.items():
            if synergy.match(group, level):
                weight, scale = perk
                return scale(team, group, weight)
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
        6: (0.8, per_member),
        4: (0.6, per_member),
        2: (0.4, per_member),
    }


class Dragon(Origin):
    levels = {
        2: (1, per_member),
    }

class Exile(Origin):
    levels = {
        1: (1, per_member),
    }

class Glacial(Origin):
    levels = {
        6: (0.45, per_member),
        4: (0.3, per_member),
        2: (0.2, per_member),
    }

class Imperial(Origin):
    levels = {
        4: (1, per_member),
        2: (1, random_member),
    }

class Ninja(Origin):
    match = exactly
    levels = {
        4: (0.8, per_member),
        1: (0.4, per_member),
    }

class Noble(Origin):
    levels = {
        6: (1.35, per_teammate),
        3: (1.35, random_teammate),
    }

class Phantom(Origin):
    levels = {
        2: (1, static_effect),
    }

class Pirate(Origin):
    levels = {
        3: (0.2, static_effect),
    }

class Robot(Origin):
    levels = {
        1: (0.1, per_member),
    }

class Void(Origin):
    levels = {
        3: (0.5, per_teammate),
    }

class Wild(Origin):
    levels = {
        4: (0.35, per_teammate),
        2: (0.35, per_member),
    }

class Yordle(Origin):
    levels = {
        6: (0.6, per_member),
        3: (0.25, per_member),
    }
    
class Assassin(Class):
    levels = {
        6: (0.35, per_member),
        3: (0.15, per_member),
    }

class Blademaster(Class):
    levels = {
        6: (0.9, per_member),
        3: (0.45, per_member),
    }

class Brawler(Class):
    levels = {
        4: (0.7, per_member),
        2: (0.3, per_member),
    }

class Elementalist(Class):
    levels = {
        3: (1, static_effect),
    }

class Guardian(Class):
    levels = {
        2: (0.4, per_teammate),
    }

class Gunslinger(Class):
    levels = {
        4: (1, per_member),
        2: (0.5, per_member),
    }

class Knight(Class):
    levels = {
        6: (0.8, per_member),
        4: (0.4, per_member),
        2: (0.2, per_member),
    }

class Ranger(Class):
    levels = {
        4: (0.65, per_member),
        2: (0.25, per_member),
    }

class Shapeshifter(Class):
    levels = {
        3: (1, per_member),
    }

class Sorcerer(Class):
    levels = {
        4: (1, per_teammate),
        2: (0.35, per_teammate),
    }
