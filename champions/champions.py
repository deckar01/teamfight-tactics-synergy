from synergies import *

class Champion:
    @classmethod
    def list(champion):
        return champion.__subclasses__()

@Demon
@Blademaster
class Aatrox(Champion):
    tier = 3
    weight = 0.1

@Wild
@Sorcerer
class Ahri(Champion):
    tier = 2
    weight = 0.7

@Ninja
@Assassin
class Akali(Champion):
    tier = 4
    weight = 0.7

@Glacial
@Elementalist
class Anivia(Champion):
    tier = 5
    weight = 0.7

@Glacial
@Ranger
class Ashe(Champion):
    tier = 3
    weight = 0.85

@Dragon
@Sorcerer
class AurelionSol(Champion):
    tier = 4
    weight = 1

@Robot
@Brawler
class Blitzcrank(Champion):
    tier = 2
    weight = 0.7

@Demon
@Elementalist
class Brand(Champion):
    tier = 4
    weight = 0.85

@Glacial
@Guardian
class Braum(Champion):
    tier = 2
    weight = 0.4

@Void
@Brawler
class ChoGath(Champion):
    tier = 4
    weight = 0.55

@Imperial
@Knight
class Darius(Champion):
    tier = 1
    weight = 0.7

@Imperial
@Blademaster
class Draven(Champion):
    tier = 4
    weight = 1

@Demon
@Shapeshifter
class Elise(Champion):
    tier = 2
    weight = 0.25

@Demon
@Assassin
class Evelynn(Champion):
    tier = 3
    weight = 0.4

@Noble
@Blademaster
class Fiora(Champion):
    tier = 1
    weight = 0.4

@Pirate
@Blademaster
@Gunslinger
class Gangplank(Champion):
    tier = 3
    weight = 0.25

@Noble
@Knight
class Garen(Champion):
    tier = 1
    weight = 1

@Wild
@Yordle
@Shapeshifter
class Gnar(Champion):
    tier = 4
    weight = 1

@Pirate
@Gunslinger
class Graves(Champion):
    tier = 1
    weight = 0.1

@Phantom
@Sorcerer
class Karthus(Champion):
    tier = 5
    weight = 0.4

@Void
@Sorcerer
class Kassadin(Champion):
    tier = 1
    weight = 0.55

@Imperial
@Assassin
class Katarina(Champion):
    tier = 3
    weight = 0.7

@Noble
@Knight
class Kayle(Champion):
    tier = 5
    weight = 0.85

@Ninja
@Yordle
@Elementalist
class Kennen(Champion):
    tier = 3
    weight = 0.55

@Void
@Assassin
class KhaZix(Champion):
    tier = 1
    weight = 0.55

@Phantom
@Ranger
class Kindred(Champion):
    tier = 4
    weight = 0.85

@Noble
@Guardian
class Leona(Champion):
    tier = 4
    weight = 0.4

@Glacial
@Elementalist
class Lissandra(Champion):
    tier = 2
    weight = 0.55

@Noble
@Gunslinger
class Lucian(Champion):
    tier = 2
    weight = 0.7

@Yordle
@Sorcerer
class Lulu(Champion):
    tier = 2
    weight = 0.85

@Pirate
@Gunslinger
class MissFortune(Champion):
    tier = 5
    weight = 0.55

@Phantom
@Knight
class Mordekaiser(Champion):
    tier = 1
    weight = 0.55

@Demon
@Sorcerer
class Morgana(Champion):
    tier = 3
    weight = 0.55

@Wild
@Shapeshifter
class Nidalee(Champion):
    tier = 1
    weight = 0.85

@Yordle
@Knight
class Poppy(Champion):
    tier = 3
    weight = 0.25

@Pirate
@Assassin
class Pyke(Champion):
    tier = 2
    weight = 1

@Void
@Brawler
class RekSai(Champion):
    tier = 2
    weight = 0.25

@Wild
@Assassin
class Rengar(Champion):
    tier = 3
    weight = 0.55

@Glacial
@Knight
class Sejuani(Champion):
    tier = 4
    weight = 1

@Ninja
@Blademaster
class Shen(Champion):
    tier = 2
    weight = 0.4

@Dragon
@Shapeshifter
class Shyvana(Champion):
    tier = 3
    weight = 0.55

@Demon
@Imperial
@Shapeshifter
class Swain(Champion):
    tier = 5
    weight = 0.85

@Yordle
@Gunslinger
class Tristana(Champion):
    tier = 1
    weight = 0.7

# @Pirate
# @Sorcerer
# class TwistedFate(Champion):
#     tier = 2

@Demon
@Ranger
class Varus(Champion):
    tier = 2
    weight = 0.7

@Noble
@Ranger
class Vayne(Champion):
    tier = 1
    weight = 0.55

@Yordle
@Sorcerer
class Veigar(Champion):
    tier = 3
    weight = 0.55

@Glacial
@Brawler
class Volibear(Champion):
    tier = 3
    weight = 0.7

@Wild
@Brawler
class Warwick(Champion):
    tier = 1
    weight = 0.55

@Exile
@Blademaster
class Yasuo(Champion):
    tier = 5
    weight = 0.55

@Ninja
@Assassin
class Zed(Champion):
    tier = 2
    weight = 0.4
