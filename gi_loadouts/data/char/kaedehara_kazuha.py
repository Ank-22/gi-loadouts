from gi_loadouts.type.char import BaseStat, Char
from gi_loadouts.type.rare import Rare
from gi_loadouts.type.stat import STAT
from gi_loadouts.type.vson import Vision
from gi_loadouts.type.weap import WeaponType


class KaedeharaKazuha(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 28.8, 3: 57.6, 4: 57.6, 5: 86.4, 6: 115.2}
    __statname__: STAT = STAT.elemental_mastery
    name: str = "Kaedehara Kazuha"
    rare: Rare = Rare.Star_5
    base: BaseStat = BaseStat(attack=23.0888, defense=62.8215, health_points=1039.1188)
    ascn: BaseStat = BaseStat(attack=94.80817, defense=257.985, health_points=4267.1836)
    weapon: WeaponType = WeaponType.sword
    vision: Vision = Vision.anemo
    cons_name: str = "Acer Palmatum"
    afln: str = "The Crux"
    head: str = "Scarlet Leaves Pursue Wild Waves"