from gi_loadouts.type.char import BaseStat, Char
from gi_loadouts.type.rare import Rare
from gi_loadouts.type.stat import STAT
from gi_loadouts.type.vson import Vision
from gi_loadouts.type.weap import WeaponType


class Collei(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 6.0, 3: 12.0, 4: 12.0, 5: 18.0, 6: 24.0}
    __statname__: STAT = STAT.attack_perc
    name: str = "Collei"
    rare: Rare = Rare.Star_4
    base: BaseStat = BaseStat(attack=16.73952, defense=50.358, health_points=820.6119)
    ascn: BaseStat = BaseStat(attack=59.895107, defense=180.18, health_points=2936.1348)
    weapon: WeaponType = WeaponType.bow
    vision: Vision = Vision.dendro
    cons_name: str = "Leptailurus Cervarius"
    afln: str = "Gandharva Ville"
    head: str = "Sprout of Rebirth"