from gi_loadouts.type.char import BaseStat, Char
from gi_loadouts.type.rare import Rare
from gi_loadouts.type.stat import STAT
from gi_loadouts.type.vson import Vision
from gi_loadouts.type.weap import WeaponType


class Arlecchino(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 9.6, 3: 19.2, 4: 19.2, 5: 28.8, 6: 38.4}
    __statname__: STAT = STAT.critical_damage_perc
    name: str = "Arlecchino"
    rare: Rare = Rare.Star_5
    base: BaseStat = BaseStat(attack=26.6266, defense=59.53085, health_points=1020.0524)
    ascn: BaseStat = BaseStat(attack=109.33523, defense=244.4715, health_points=4188.8867)
    weapon: WeaponType = WeaponType.polearm
    vision: Vision = Vision.pyro
    cons_name: str = "Ignis Purgatorius"
    afln: str = "Fatui"
    head: str = "Dire Balemoon"