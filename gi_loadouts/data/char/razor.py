from gi_loadouts.type.char import BaseStat, Char
from gi_loadouts.type.rare import Rare
from gi_loadouts.type.stat import STAT
from gi_loadouts.type.vson import Vision
from gi_loadouts.type.weap import WeaponType


class Razor(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 7.5, 3: 15.0, 4: 15.0, 5: 22.5, 6: 30.0}
    __statname__: STAT = STAT.damage_bonus_physical_perc
    name: str = "Razor"
    rare: Rare = Rare.Star_4
    base: BaseStat = BaseStat(attack=19.5888, defense=62.9475, health_points=1002.9701)
    ascn: BaseStat = BaseStat(attack=70.09002, defense=225.225, health_points=3588.6091)
    weapon: WeaponType = WeaponType.claymore
    vision: Vision = Vision.electro
    cons_name: str = "Lupus Minor"
    afln: str = "Wolvendom"
    head: str = "Wolf Boy"