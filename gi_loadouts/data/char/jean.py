from gi_loadouts.type.char import BaseStat, Char
from gi_loadouts.type.rare import Rare
from gi_loadouts.type.stat import STAT
from gi_loadouts.type.vson import Vision
from gi_loadouts.type.weap import WeaponType


class Jean(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 5.5, 3: 11.0, 4: 11.0, 5: 16.5, 6: 22.0}
    __statname__: STAT = STAT.healing_bonus_perc
    name: str = "Jean"
    rare: Rare = Rare.Star_5
    base: BaseStat = BaseStat(attack=18.62, defense=59.83, health_points=1143.984)
    ascn: BaseStat = BaseStat(attack=76.4582, defense=245.7, health_points=4697.817)
    weapon: WeaponType = WeaponType.sword
    vision: Vision = Vision.anemo
    cons_name: str = "Leo Minor"
    afln: str = "Knights of Favonius"
    head: str = "Dandelion Knight"