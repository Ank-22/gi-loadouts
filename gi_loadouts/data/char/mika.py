from gi_loadouts.type.char import BaseStat, Char
from gi_loadouts.type.rare import Rare
from gi_loadouts.type.stat import STAT
from gi_loadouts.type.vson import Vision
from gi_loadouts.type.weap import WeaponType


class Mika(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 6.0, 3: 12.0, 4: 12.0, 5: 18.0, 6: 24.0}
    __statname__: STAT = STAT.health_points_perc
    name: str = "Mika"
    rare: Rare = Rare.Star_4
    base: BaseStat = BaseStat(attack=18.6984, defense=59.800125, health_points=1048.5597)
    ascn: BaseStat = BaseStat(attack=66.90411, defense=213.96375, health_points=3751.7275)
    weapon: WeaponType = WeaponType.polearm
    vision: Vision = Vision.cryo
    cons_name: str = "Palumbus"
    afln: str = "Knights of Favonius"
    head: str = "Coordinates of Clear Frost"