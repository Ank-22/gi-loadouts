from gi_loadouts.type.char import BaseStat, Char
from gi_loadouts.type.rare import Rare
from gi_loadouts.type.stat import STAT
from gi_loadouts.type.vson import Vision
from gi_loadouts.type.weap import WeaponType


class Diona(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 4.8, 3: 9.6, 4: 9.6, 5: 14.4, 6: 19.2}
    __statname__: STAT = STAT.damage_bonus_cryo_perc
    name: str = "Diona"
    rare: Rare = Rare.Star_4
    base: BaseStat = BaseStat(attack=17.808, defense=50.358, health_points=802.3761)
    ascn: BaseStat = BaseStat(attack=63.7182, defense=180.18, health_points=2870.8872)
    weapon: WeaponType = WeaponType.bow
    vision: Vision = Vision.cryo
    cons_name: str = "Feles"
    afln: str = "The Cat's Tail"
    head: str = "Kätzlein Cocktail"