from gi_loadouts.type.char import BaseStat, Char
from gi_loadouts.type.rare import Rare
from gi_loadouts.type.stat import STAT
from gi_loadouts.type.vson import Vision
from gi_loadouts.type.weap import WeaponType


class Diluc(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 4.8, 3: 9.6, 4: 9.6, 5: 14.4, 6: 19.2}
    __statname__: STAT = STAT.critical_rate_perc
    name: str = "Diluc"
    rare: Rare = Rare.Star_5
    base: BaseStat = BaseStat(attack=26.068, defense=61.0266, health_points=1010.5192)
    ascn: BaseStat = BaseStat(attack=107.04148, defense=250.614, health_points=4149.7383)
    weapon: WeaponType = WeaponType.claymore
    vision: Vision = Vision.pyro
    cons_name: str = "Noctua"
    afln: str = "Dawn Winery"
    head: str = "The Dark Side of Dawn"