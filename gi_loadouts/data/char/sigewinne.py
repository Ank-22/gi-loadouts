from gi_loadouts.type.char import BaseStat, Char
from gi_loadouts.type.rare import Rare
from gi_loadouts.type.stat import STAT
from gi_loadouts.type.vson import Vision
from gi_loadouts.type.weap import WeaponType


class Sigewinne(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 7.2, 3: 14.4, 4: 14.4, 5: 21.6, 6: 28.8}
    __statname__: STAT = STAT.healing_bonus_perc
    name: str = "Sigewinne"
    rare: Rare = Rare.Star_5
    base: BaseStat = BaseStat(attack=14.9891, defense=38.8895, health_points=1039.1188)
    ascn: BaseStat = BaseStat(attack=61.54885, defense=159.705, health_points=4267.1836)
    weapon: WeaponType = WeaponType.bow
    vision: Vision = Vision.hydro
    cons_name: str = "Nereides"
    afln: str = "Fortress of Meropide"
    head: str = "Wondrous Dragonheir"