from gi_loadouts.type.char import BaseStat, Char
from gi_loadouts.type.rare import Rare
from gi_loadouts.type.stat import STAT
from gi_loadouts.type.vson import Vision
from gi_loadouts.type.weap import WeaponType


class Dehya(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 7.2, 3: 14.4, 4: 14.4, 5: 21.6, 6: 28.8}
    __statname__: STAT = STAT.health_points_perc
    name: str = "Dehya"
    rare: Rare = Rare.Star_5
    base: BaseStat = BaseStat(attack=20.6682, defense=48.88111, health_points=1220.2496)
    ascn: BaseStat = BaseStat(attack=84.8686, defense=200.7369, health_points=5011.0044)
    weapon: WeaponType = WeaponType.claymore
    vision: Vision = Vision.pyro
    cons_name: str = "Mantichora"
    afln: str = "The Eremites"
    head: str = "Flame-Mane"