# Teamfight Tactics Synergies

Find team synergies that provide the biggest bonuses.

## Requirements

- Python 3

## Use

```sh
usage: teams.py [-h] [-s SIZE] [-t TOP]

optional arguments:
  -h, --help            show this help message and exit
  -s SIZE, --size SIZE  The size of the teams. Defaults to 3.
  -t TOP, --top TOP     The number of teams to show. Defaults to 10.
```

**Example**

```sh
$ ./teams.py --size=3 --top=1
Ahri, Lulu, Nidalee
2 Sorcerers, 2 Wilds
Bonus: 3.7825
```

## TODO

- Optimize search with A* to try extending good partial synergies first.
- Include champion stats in team scoring
- Apply actual bonuses to champion stats
- Consider tank/magic/damage/support balance in the scoring
