from gi_loadouts.type.char import BaseStat, Char
from gi_loadouts.type.rare import Rare
from gi_loadouts.type.stat import STAT
from gi_loadouts.type.vson import Vision
from gi_loadouts.type.weap import WeaponType


class Rosaria(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 6.0, 3: 12.0, 4: 12.0, 5: 18.0, 6: 24.0}
    __statname__: STAT = STAT.attack_perc
    name: str = "Rosaria"
    rare: Rare = Rare.Star_4
    base: BaseStat = BaseStat(attack=20.12304, defense=59.514, health_points=1030.3239)
    ascn: BaseStat = BaseStat(attack=72.001564, defense=212.94, health_points=3686.4802)
    weapon: WeaponType = WeaponType.polearm
    vision: Vision = Vision.cryo
    cons_name: str = "Spinea Corona"
    afln: str = "Church of Favonius"
    head: str = "Thorny Benevolence"