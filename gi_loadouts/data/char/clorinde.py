from gi_loadouts.type.char import BaseStat, Char
from gi_loadouts.type.rare import Rare
from gi_loadouts.type.stat import STAT
from gi_loadouts.type.vson import Vision
from gi_loadouts.type.weap import WeaponType


class Clorinde(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 4.8, 3: 9.6, 4: 9.6, 5: 14.4, 6: 19.2}
    __statname__: STAT = STAT.critical_rate_perc
    name: str = "Clorinde"
    rare: Rare = Rare.Star_5
    base: BaseStat = BaseStat(attack=26.2542, defense=61.0266, health_points=1008.61255)
    ascn: BaseStat = BaseStat(attack=107.80606, defense=250.614, health_points=4141.908)
    weapon: WeaponType = WeaponType.sword
    vision: Vision = Vision.electro
    cons_name: str = "Rapperia"
    afln: str = "Trial Court"
    head: str = "Candlebearer, Shadowhunter"