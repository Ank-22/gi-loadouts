from gi_loadouts.type.char import BaseStat, Char
from gi_loadouts.type.rare import Rare
from gi_loadouts.type.stat import STAT
from gi_loadouts.type.vson import Vision
from gi_loadouts.type.weap import WeaponType


class Barbara(Char):
    __statdata__: dict = {0: 0.0, 1: 0.0, 2: 6.0, 3: 12.0, 4: 12.0, 5: 18.0, 6: 24.0}
    __statname__: STAT = STAT.health_points_perc
    name: str = "Barbara"
    rare: Rare = Rare.Star_4
    base: BaseStat = BaseStat(attack=13.356, defense=56.0805, health_points=820.6119)
    ascn: BaseStat = BaseStat(attack=47.78865, defense=200.655, health_points=2936.1348)
    weapon: WeaponType = WeaponType.catalyst
    vision: Vision = Vision.hydro
    cons_name: str = "Crater"
    afln: str = "Church of Favonius"
    head: str = "Shining Idol"