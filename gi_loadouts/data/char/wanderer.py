from gi_loadouts.type.char import BaseStat, Char
from gi_loadouts.type.rare import Rare
from gi_loadouts.type.stat import STAT
from gi_loadouts.type.vson import Vision
from gi_loadouts.type.weap import WeaponType


class Wanderer(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 4.8, 3: 9.6, 4: 9.6, 5: 14.4, 6: 19.2}
    __statname__: STAT = STAT.critical_rate_perc
    name: str = "Wanderer"
    rare: Rare = Rare.Star_5
    base: BaseStat = BaseStat(attack=25.5094, defense=47.2657, health_points=791.2556)
    ascn: BaseStat = BaseStat(attack=104.747734, defense=194.103, health_points=3249.3232)
    weapon: WeaponType = WeaponType.catalyst
    vision: Vision = Vision.anemo
    cons_name: str = "Peregrinus"
    head: str = "Eons Adrift"