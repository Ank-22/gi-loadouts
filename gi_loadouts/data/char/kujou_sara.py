from gi_loadouts.type.char import BaseStat, Char
from gi_loadouts.type.rare import Rare
from gi_loadouts.type.stat import STAT
from gi_loadouts.type.vson import Vision
from gi_loadouts.type.weap import WeaponType


class KujouSara(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 6.0, 3: 12.0, 4: 12.0, 5: 18.0, 6: 24.0}
    __statname__: STAT = STAT.attack_perc
    name: str = "Kujou Sara"
    rare: Rare = Rare.Star_4
    base: BaseStat = BaseStat(attack=16.38336, defense=52.647, health_points=802.3761)
    ascn: BaseStat = BaseStat(attack=58.620743, defense=188.37, health_points=2870.8872)
    weapon: WeaponType = WeaponType.bow
    vision: Vision = Vision.electro
    cons_name: str = "Flabellum"
    afln: str = "Tenryou Commission"
    head: str = "Crowfeather Kaburaya"