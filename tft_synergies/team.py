from collections import defaultdict


class Team:
    def __init__(self, champions):
        self.champions = champions
        self.synergies = self.get_synergies()
        self.score = self.get_score()

    def get_synergies(self):
        synergies = defaultdict(list)
        for champion in self.champions:
            for synergy in champion.synergies:
                synergies[synergy].append(champion)
        return synergies

    def get_score(self):
        return sum(
            synergy.score(len(self.champions), len(champions))
            for synergy, champions in self.synergies.items()
        )

    def get_synergy_names(self):
        names = [
            synergy.name(len(self.champions), len(champions))
            for synergy, champions in self.synergies.items()
        ]
        return [name for name in names if name]

    def get_champion_names(self):
        return [champion.__name__ for champion in self.champions]
    
    def __lt__(team, other):
        return team.score < other.score
    
    def __eq__(team, other):
        return team.score == other.score
