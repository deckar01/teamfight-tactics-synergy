from .synergies import *

class Champion:
    @classmethod
    def list(champion):
        return champion.__subclasses__()

@Demon
@Blademaster
class Aatrox(Champion):
    tier = 3

@Wild
@Sorcerer
class Ahri(Champion):
    tier = 2

@Ninja
@Assassin
class Akali(Champion):
    tier = 4

@Glacial
@Elementalist
class Anivia(Champion):
    tier = 5

@Glacial
@Ranger
class Ashe(Champion):
    tier = 3

@Dragon
@Sorcerer
class AurelionSol(Champion):
    tier = 4

@Robot
@Brawler
class Blitzcrank(Champion):
    tier = 2

@Demon
@Elementalist
class Brand(Champion):
    tier = 4

@Glacial
@Guardian
class Braum(Champion):
    tier = 2

@Void
@Brawler
class ChoGath(Champion):
    tier = 4

@Imperial
@Knight
class Darius(Champion):
    tier = 1

@Imperial
@Blademaster
class Draven(Champion):
    tier = 4

@Demon
@Shapeshifter
class Elise(Champion):
    tier = 2

@Demon
@Assassin
class Evelynn(Champion):
    tier = 3

@Noble
@Blademaster
class Fiora(Champion):
    tier = 1

@Pirate
@Blademaster
@Gunslinger
class Gangplank(Champion):
    tier = 3

@Noble
@Knight
class Garen(Champion):
    tier = 1

@Wild
@Yordle
@Shapeshifter
class Gnar(Champion):
    tier = 4

@Pirate
@Gunslinger
class Graves(Champion):
    tier = 1

@Phantom
@Sorcerer
class Karthus(Champion):
    tier = 5

@Void
@Sorcerer
class Kassadin(Champion):
    tier = 1

@Imperial
@Assassin
class Katarina(Champion):
    tier = 3

@Noble
@Knight
class Kayle(Champion):
    tier = 5

@Ninja
@Yordle
@Elementalist
class Kennen(Champion):
    tier = 3

@Void
@Assassin
class KhaZix(Champion):
    tier = 1

@Phantom
@Ranger
class Kindred(Champion):
    tier = 4

@Noble
@Guardian
class Leona(Champion):
    tier = 4

@Glacial
@Elementalist
class Lissandra(Champion):
    tier = 2

@Noble
@Gunslinger
class Lucian(Champion):
    tier = 2

@Yordle
@Sorcerer
class Lulu(Champion):
    tier = 2

@Pirate
@Gunslinger
class MissFortune(Champion):
    tier = 5

@Phantom
@Knight
class Mordekaiser(Champion):
    tier = 1

@Demon
@Sorcerer
class Morgana(Champion):
    tier = 3

@Wild
@Shapeshifter
class Nidalee(Champion):
    tier = 1

@Yordle
@Knight
class Poppy(Champion):
    tier = 3

@Pirate
@Assassin
class Pyke(Champion):
    tier = 2

@Void
@Brawler
class RekSai(Champion):
    tier = 2

@Wild
@Assassin
class Rengar(Champion):
    tier = 3

@Glacial
@Knight
class Sejuani(Champion):
    tier = 4

@Ninja
@Blademaster
class Shen(Champion):
    tier = 2

@Dragon
@Shapeshifter
class Shyvana(Champion):
    tier = 3

@Demon
@Imperial
@Shapeshifter
class Swain(Champion):
    tier = 5

@Yordle
@Gunslinger
class Tristana(Champion):
    tier = 1

@Pirate
@Sorcerer
class TwistedFate(Champion):
    tier = 2

@Demon
@Ranger
class Varus(Champion):
    tier = 2

@Noble
@Ranger
class Vayne(Champion):
    tier = 1

@Yordle
@Sorcerer
class Veigar(Champion):
    tier = 3

@Glacial
@Brawler
class Volibear(Champion):
    tier = 3

@Wild
@Brawler
class Warwick(Champion):
    tier = 1

@Exile
@Blademaster
class Yasuo(Champion):
    tier = 5

@Ninja
@Assassin
class Zed(Champion):
    tier = 2
