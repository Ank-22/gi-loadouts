from gi_loadouts.type.char import BaseStat, Char
from gi_loadouts.type.rare import Rare
from gi_loadouts.type.stat import STAT
from gi_loadouts.type.vson import Vision
from gi_loadouts.type.weap import WeaponType


class Sethos(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 24.0, 3: 48.0, 4: 48.0, 5: 72.0, 6: 96.0}
    __statname__: STAT = STAT.elemental_mastery
    name: str = "Sethos"
    rare: Rare = Rare.Star_4
    base: BaseStat = BaseStat(attack=19.05456, defense=46.9245, health_points=820.6119)
    ascn: BaseStat = BaseStat(attack=68.178474, defense=167.895, health_points=2936.1348)
    weapon: WeaponType = WeaponType.bow
    vision: Vision = Vision.electro
    cons_name: str = "Basileos Delta"
    afln: str = "Temple of Silence"
    head: str = "Wisdom's Measure"