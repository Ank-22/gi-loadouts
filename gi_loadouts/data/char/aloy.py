from gi_loadouts.type.char import BaseStat, Char
from gi_loadouts.type.rare import Rare
from gi_loadouts.type.stat import STAT
from gi_loadouts.type.vson import Vision
from gi_loadouts.type.weap import WeaponType


class Aloy(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 7.2, 3: 14.4, 4: 14.4, 5: 21.6, 6: 28.8}
    __statname__: STAT = STAT.damage_bonus_cryo_perc
    name: str = "Aloy"
    rare: Rare = Rare.Star_5
    base: BaseStat = BaseStat(attack=18.21036, defense=52.6504, health_points=848.4548)
    ascn: BaseStat = BaseStat(attack=74.77612, defense=216.216, health_points=3484.214)
    weapon: WeaponType = WeaponType.bow
    vision: Vision = Vision.cryo
    cons_name: str = "Nora Fortis"
    afln: str = "Wandering Heroine"
    head: str = "Savior From Another World"