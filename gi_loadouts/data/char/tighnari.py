from gi_loadouts.type.char import BaseStat, Char
from gi_loadouts.type.rare import Rare
from gi_loadouts.type.stat import STAT
from gi_loadouts.type.vson import Vision
from gi_loadouts.type.weap import WeaponType


class Tighnari(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 7.2, 3: 14.4, 4: 14.4, 5: 21.6, 6: 28.8}
    __statname__: STAT = STAT.damage_bonus_dendro_perc
    name: str = "Tighnari"
    rare: Rare = Rare.Star_5
    base: BaseStat = BaseStat(attack=20.8544, defense=49.0606, health_points=844.64154)
    ascn: BaseStat = BaseStat(attack=85.63319, defense=201.474, health_points=3468.5547)
    weapon: WeaponType = WeaponType.bow
    vision: Vision = Vision.dendro
    cons_name: str = "Vulpes Zerda"
    afln: str = "Gandharva Ville"
    head: str = "Verdant Strider"