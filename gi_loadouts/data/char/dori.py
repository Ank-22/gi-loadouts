from gi_loadouts.type.char import BaseStat, Char
from gi_loadouts.type.rare import Rare
from gi_loadouts.type.stat import STAT
from gi_loadouts.type.vson import Vision
from gi_loadouts.type.weap import WeaponType


class Dori(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 6.0, 3: 12.0, 4: 12.0, 5: 18.0, 6: 24.0}
    __statname__: STAT = STAT.health_points_perc
    name: str = "Dori"
    rare: Rare = Rare.Star_4
    base: BaseStat = BaseStat(attack=18.6984, defense=60.6585, health_points=1039.4418)
    ascn: BaseStat = BaseStat(attack=66.90411, defense=217.035, health_points=3719.104)
    weapon: WeaponType = WeaponType.catalyst
    vision: Vision = Vision.electro
    cons_name: str = "Magicae Lucerna"
    afln: str = "The Palace of Alcazarzaray"
    head: str = "Treasure of Dream Garden"