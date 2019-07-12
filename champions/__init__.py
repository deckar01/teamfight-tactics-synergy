import sys
from itertools import combinations
from heapq import heappush, heappop

from champions import Champion
from team import Team
from odds import champion_drop_rate

if __name__ == '__main__':
    team_size = int(sys.argv[1])
    available_champions = [
        champion
        for champion in Champion.list()
        if champion_drop_rate[team_size][champion.tier - 1]
    ]
    teams = []
    for picks in combinations(available_champions, team_size):
        team = Team(picks)
        heappush(teams, team)
        if len(teams) > 10:
            heappop(teams)
    teams.sort()
    for team in teams:
        print(', '.join(team.get_champion_names()))
        print(', '.join(team.get_synergy_names()))
        print('{:0.4f}'.format(team.score))
        print('')
