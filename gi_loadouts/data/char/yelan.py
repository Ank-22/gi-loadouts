from gi_loadouts.type.char import BaseStat, Char
from gi_loadouts.type.rare import Rare
from gi_loadouts.type.stat import STAT
from gi_loadouts.type.vson import Vision
from gi_loadouts.type.weap import WeaponType


class Yelan(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 4.8, 3: 9.6, 4: 9.6, 5: 14.4, 6: 19.2}
    __statname__: STAT = STAT.critical_rate_perc
    name: str = "Yelan"
    rare: Rare = Rare.Star_5
    base: BaseStat = BaseStat(attack=18.9924, defense=42.65879, health_points=1124.9176)
    ascn: BaseStat = BaseStat(attack=77.987366, defense=175.1841, health_points=4619.52)
    weapon: WeaponType = WeaponType.bow
    vision: Vision = Vision.hydro
    cons_name: str = "Umbrabilis Orchis"
    afln: str = "Yanshang Teahouse"
    head: str = "Valley Orchid"