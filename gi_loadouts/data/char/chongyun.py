from gi_loadouts.type.char import BaseStat, Char
from gi_loadouts.type.rare import Rare
from gi_loadouts.type.stat import STAT
from gi_loadouts.type.vson import Vision
from gi_loadouts.type.weap import WeaponType


class Chongyun(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 6.0, 3: 12.0, 4: 12.0, 5: 18.0, 6: 24.0}
    __statname__: STAT = STAT.attack_perc
    name: str = "Chongyun"
    rare: Rare = Rare.Star_4
    base: BaseStat = BaseStat(attack=18.6984, defense=54.36375, health_points=920.90894)
    ascn: BaseStat = BaseStat(attack=66.90411, defense=194.5125, health_points=3294.9956)
    weapon: WeaponType = WeaponType.claymore
    vision: Vision = Vision.cryo
    cons_name: str = "Nubis Caesor"
    afln: str = "Tianheng Thaumaturges"
    head: str = "Frozen Ardor"