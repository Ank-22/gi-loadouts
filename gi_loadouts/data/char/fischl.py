from gi_loadouts.type.char import BaseStat, Char
from gi_loadouts.type.rare import Rare
from gi_loadouts.type.stat import STAT
from gi_loadouts.type.vson import Vision
from gi_loadouts.type.weap import WeaponType


class Fischl(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 6.0, 3: 12.0, 4: 12.0, 5: 18.0, 6: 24.0}
    __statname__: STAT = STAT.attack_perc
    name: str = "Fischl"
    rare: Rare = Rare.Star_4
    base: BaseStat = BaseStat(attack=20.4792, defense=49.78575, health_points=770.4634)
    ascn: BaseStat = BaseStat(attack=73.27593, defense=178.1325, health_points=2756.704)
    weapon: WeaponType = WeaponType.bow
    vision: Vision = Vision.electro
    cons_name: str = "Corvus"
    afln: str = "Adventurers' Guild"
    head: str = "Prinzessin der Verurteilung!"