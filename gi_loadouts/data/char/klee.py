from gi_loadouts.type.char import BaseStat, Char
from gi_loadouts.type.rare import Rare
from gi_loadouts.type.stat import STAT
from gi_loadouts.type.vson import Vision
from gi_loadouts.type.weap import WeaponType


class Klee(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 7.2, 3: 14.4, 4: 14.4, 5: 21.6, 6: 28.8}
    __statname__: STAT = STAT.damage_bonus_pyro_perc
    name: str = "Klee"
    rare: Rare = Rare.Star_5
    base: BaseStat = BaseStat(attack=24.206, defense=47.864, health_points=800.7888)
    ascn: BaseStat = BaseStat(attack=99.39566, defense=196.56, health_points=3288.4717)
    weapon: WeaponType = WeaponType.catalyst
    vision: Vision = Vision.pyro
    cons_name: str = "Trifolium"
    afln: str = "Knights of Favonius"
    head: str = "Fleeing Sunlight"