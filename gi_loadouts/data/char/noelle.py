from gi_loadouts.type.char import BaseStat, Char
from gi_loadouts.type.rare import Rare
from gi_loadouts.type.stat import STAT
from gi_loadouts.type.vson import Vision
from gi_loadouts.type.weap import WeaponType


class Noelle(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 7.5, 3: 15.0, 4: 15.0, 5: 22.5, 6: 30.0}
    __statname__: STAT = STAT.defense_perc
    name: str = "Noelle"
    rare: Rare = Rare.Star_4
    base: BaseStat = BaseStat(attack=16.0272, defense=66.95325, health_points=1012.088)
    ascn: BaseStat = BaseStat(attack=57.34638, defense=239.5575, health_points=3621.2327)
    weapon: WeaponType = WeaponType.claymore
    vision: Vision = Vision.geo
    cons_name: str = "Parma Cordis"
    afln: str = "Knights of Favonius"
    head: str = "Chivalric Blossom"