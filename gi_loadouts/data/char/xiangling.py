from gi_loadouts.type.char import BaseStat, Char
from gi_loadouts.type.rare import Rare
from gi_loadouts.type.stat import STAT
from gi_loadouts.type.vson import Vision
from gi_loadouts.type.weap import WeaponType


class Xiangling(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 24.0, 3: 48.0, 4: 48.0, 5: 72.0, 6: 96.0}
    __statname__: STAT = STAT.elemental_mastery
    name: str = "Xiangling"
    rare: Rare = Rare.Star_4
    base: BaseStat = BaseStat(attack=18.87648, defense=56.0805, health_points=911.791)
    ascn: BaseStat = BaseStat(attack=67.54129, defense=200.655, health_points=3262.3718)
    weapon: WeaponType = WeaponType.polearm
    vision: Vision = Vision.pyro
    cons_name: str = "Trulla"
    afln: str = "Wanmin Restaurant"
    head: str = "Exquisite Delicacy"