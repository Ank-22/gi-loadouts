from gi_loadouts.type.char import BaseStat, Char
from gi_loadouts.type.rare import Rare
from gi_loadouts.type.stat import STAT
from gi_loadouts.type.vson import Vision
from gi_loadouts.type.weap import WeaponType


class Thoma(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 6.0, 3: 12.0, 4: 12.0, 5: 18.0, 6: 24.0}
    __statname__: STAT = STAT.attack_perc
    name: str = "Thoma"
    rare: Rare = Rare.Star_4
    base: BaseStat = BaseStat(attack=16.9176, defense=62.9475, health_points=866.2015)
    ascn: BaseStat = BaseStat(attack=60.53229, defense=225.225, health_points=3099.2532)
    weapon: WeaponType = WeaponType.polearm
    vision: Vision = Vision.pyro
    cons_name: str = "Rubeum Scutum"
    afln: str = "Yashiro Commission"
    head: str = "Protector From Afar"