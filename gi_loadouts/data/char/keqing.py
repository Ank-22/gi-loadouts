from gi_loadouts.type.char import BaseStat, Char
from gi_loadouts.type.rare import Rare
from gi_loadouts.type.stat import STAT
from gi_loadouts.type.vson import Vision
from gi_loadouts.type.weap import WeaponType


class Keqing(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 9.6, 3: 19.2, 4: 19.2, 5: 28.8, 6: 38.4}
    __statname__: STAT = STAT.critical_damage_perc
    name: str = "Keqing"
    rare: Rare = Rare.Star_5
    base: BaseStat = BaseStat(attack=25.137, defense=62.2232, health_points=1020.0524)
    ascn: BaseStat = BaseStat(attack=103.21857, defense=255.528, health_points=4188.8867)
    weapon: WeaponType = WeaponType.sword
    vision: Vision = Vision.electro
    cons_name: str = "Trulla Cementarii"
    afln: str = "Liyue Qixing"
    head: str = "Driving Thunder"