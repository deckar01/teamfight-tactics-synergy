#!/usr/local/bin/python3

import sys
import argparse
from itertools import combinations
from heapq import heappush, heappop

from tft_synergies.champions import Champion
from tft_synergies.team import Team
from tft_synergies.odds import champion_drop_rate


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-s',
        '--size',
        type=int,
        default=3,
        help='The size of the teams. Defaults to 3.',
    )
    parser.add_argument(
        '-t',
        '--top',
        type=int,
        default=10,
        help='The number of teams to show. Defaults to 10.',
    )
    args = parser.parse_args()
    # Ignore champion tiers that are not available at the current team size.
    available_champions = [
        champion
        for champion in Champion.list()
        if champion_drop_rate[args.size][champion.tier - 1]
    ]
    teams = []
    # TODO: Use A* to try good partial teams first.
    for picks in combinations(available_champions, args.size):
        team = Team(picks)
        # Store the teams in a heap to optimize sorted inserts.
        heappush(teams, team)
        # Only keep the best teams in the heap.
        if len(teams) > args.top:
            heappop(teams)
    teams.sort()
    for team in teams:
        print(', '.join(team.get_champion_names()))
        print(', '.join(team.get_synergy_names()))
        print('Bonus: {:0.4f}'.format(team.score))
        print('')
